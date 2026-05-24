"""API-key authentication dependency for the governance service."""
from __future__ import annotations

import logging
import os
import secrets

from fastapi import Header, HTTPException, status

logger = logging.getLogger(__name__)

_API_KEY = os.getenv("KDD_INTERNAL_API_KEY", "")
if not _API_KEY:
    logger.warning(
        "KDD_INTERNAL_API_KEY is not set — all protected endpoints are OPEN. "
        "Set this env var in production."
    )


async def require_api_key(x_api_key: str = Header(default="", alias="X-API-Key")) -> None:
    """Reject requests that do not carry a valid internal API key.

    If KDD_INTERNAL_API_KEY is not configured (dev mode) every request is
    allowed, but a warning is emitted at startup so the gap is visible.
    """
    if not _API_KEY:
        return  # dev / CI — open by design, warned at startup
    if not secrets.compare_digest(x_api_key, _API_KEY):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-API-Key header",
            headers={"WWW-Authenticate": "ApiKey"},
        )
