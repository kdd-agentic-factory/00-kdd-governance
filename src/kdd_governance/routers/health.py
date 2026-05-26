"""Health endpoint for governance-policy-service."""
import os
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    environment: str


@router.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(
        status="ok",
        service="governance-policy-service",
        version="0.1.0",
        environment=os.getenv("APP_ENV", "local"),
    )
