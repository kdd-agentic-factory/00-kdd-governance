"""KDD Governance Policy Service — validate artifacts, traceability and evidence packets."""
import logging
import os
from contextlib import asynccontextmanager

import structlog

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from fastapi import Depends

from .metrics import REQUEST_COUNT
from .middleware import RequestContextMiddleware
from .rate_limit import RateLimitMiddleware
from .routers import health, kdd, roles, version
from .security import require_api_key

logger = logging.getLogger(__name__)

SERVICE_NAME = "governance-policy-service"
VERSION = "0.1.0"


def _configure_otel(app: FastAPI, service_name: str = "governance-policy-service") -> None:
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "")
    if not endpoint:
        return
    try:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        provider = TracerProvider(resource=Resource.create({"service.name": service_name}))
        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint, insecure=True)))
        trace.set_tracer_provider(provider)
        FastAPIInstrumentor.instrument_app(app)
        logger.info("OTEL tracing enabled → %s", endpoint)
    except Exception as exc:
        logger.warning("OTEL setup failed (non-fatal): %s", exc)


@asynccontextmanager
async def lifespan(application: FastAPI):
    logger.info("Starting %s v%s", SERVICE_NAME, VERSION)
    yield
    logger.info("Shutting down %s", SERVICE_NAME)


app = FastAPI(
    title="KDD Governance Policy Service",
    version=VERSION,
    description=(
        "Defines and enforces KDD lifecycle governance across the entire platform. "
        "Validates artifacts, traceability chains, evidence packets and dataset lineage. "
        "Consumed by all services that produce or consume KDD artifacts."
    ),
    lifespan=lifespan,
)

app.add_middleware(RateLimitMiddleware, calls_per_minute=int(os.getenv("RATE_LIMIT_PER_MINUTE", "60")))
app.add_middleware(RequestContextMiddleware)
_cors_origins = [o for o in os.getenv("CORS_ORIGINS", "").split(",") if o]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins or ["*"],  # "*" only when env var is unset (local dev)
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=False,
)


@app.middleware("http")
async def _metrics_middleware(request: Request, call_next):
    response = await call_next(request)
    REQUEST_COUNT.labels(
        method=request.method, path=request.url.path, status_code=response.status_code
    ).inc()
    return response


@app.get("/metrics", include_in_schema=False)
async def _metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


_auth = [Depends(require_api_key)]
_API_V1 = "/api/v1"

app.include_router(health.router, tags=["health"])
app.include_router(version.router, tags=["version"])
app.include_router(kdd.router, prefix=f"{_API_V1}/kdd", tags=["kdd"], dependencies=_auth)
app.include_router(roles.router, prefix=f"{_API_V1}/roles", tags=["roles"], dependencies=_auth)

_configure_otel(app)

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    logger_factory=structlog.PrintLoggerFactory(),
)


def create_app() -> FastAPI:
    return app


def main() -> None:
    import uvicorn
    uvicorn.run(
        "kdd_governance.main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8090")),
        log_level="info",
    )


if __name__ == "__main__":
    main()
