"""Shared Prometheus metrics for kdd-governance."""
from prometheus_client import Counter

REQUEST_COUNT = Counter(
    "governance_http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status_code"],
)

VALIDATION_COUNT = Counter(
    "governance_validations_total",
    "Artifact validations performed",
    ["artifact_type", "valid"],
)
