"""Actor role definitions endpoint — serves actor_roles.yaml as REST."""
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from fastapi import APIRouter, HTTPException

router = APIRouter()
logger = logging.getLogger(__name__)

# Resolve path: prefer ACTOR_ROLES_PATH env var, then walk upward to find the config file
def _load_actor_roles() -> Dict[str, Any]:
    env_path = os.getenv("ACTOR_ROLES_PATH")
    if env_path:
        p = Path(env_path)
    else:
        # Walk up from this file to find 00-kdd-governance/config/actor_roles.yaml
        candidates = [
            Path(__file__).parents[5] / "00-kdd-governance" / "config" / "actor_roles.yaml",
            Path(__file__).parents[3] / "config" / "actor_roles.yaml",
            Path("/app/config/actor_roles.yaml"),
        ]
        p = next((c for c in candidates if c.exists()), None)

    if p is None or not p.exists():
        logger.warning("actor_roles.yaml not found — returning empty roles")
        return {"version": "0.0", "roles": {}, "permission_matrix": {}}

    with open(p, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    logger.info("Loaded actor roles from %s (%d roles)", p, len(data.get("roles", {})))
    return data


_ROLES_DATA: Dict[str, Any] = {}


def get_roles_data() -> Dict[str, Any]:
    global _ROLES_DATA
    if not _ROLES_DATA:
        _ROLES_DATA = _load_actor_roles()
    return _ROLES_DATA


# ── Endpoints ──────────────────────────────────────────────────────────────────

@router.get("")
async def list_roles():
    data = get_roles_data()
    roles = data.get("roles", {})
    return {
        "roles": [
            {
                "role_id": rid,
                "display_name": rdef.get("display_name", rid),
                "description": rdef.get("description", ""),
                "data_access": rdef.get("data_access", []),
                "approval_authority": rdef.get("approval_authority", []),
                "escalation_to": rdef.get("escalation_to"),
            }
            for rid, rdef in roles.items()
        ],
        "total": len(roles),
    }


@router.get("/{role_id}")
async def get_role(role_id: str):
    data = get_roles_data()
    roles = data.get("roles", {})
    if role_id not in roles:
        raise HTTPException(status_code=404, detail=f"Role '{role_id}' not found")
    rdef = roles[role_id]
    return {"role_id": role_id, **rdef}


@router.get("/{role_id}/tools")
async def get_role_tools(role_id: str):
    data = get_roles_data()
    roles = data.get("roles", {})
    if role_id not in roles:
        raise HTTPException(status_code=404, detail=f"Role '{role_id}' not found")
    return {
        "role_id": role_id,
        "mcp_tools": roles[role_id].get("mcp_tools", []),
        "allowed_skills": roles[role_id].get("allowed_skills", []),
    }


@router.get("/{role_id}/context")
async def get_role_hermes_context(role_id: str):
    """Hermes AI context prompt for this role."""
    data = get_roles_data()
    roles = data.get("roles", {})
    if role_id not in roles:
        raise HTTPException(status_code=404, detail=f"Role '{role_id}' not found")
    return {
        "role_id": role_id,
        "hermes_context": roles[role_id].get("hermes_context", ""),
    }


@router.get("/permission-matrix/full")
async def get_permission_matrix():
    data = get_roles_data()
    return data.get("permission_matrix", {})


@router.post("/check-access")
async def check_data_access(role_id: str, classification: str):
    """Return whether role_id can access data of the given classification level."""
    data = get_roles_data()
    roles = data.get("roles", {})
    if role_id not in roles:
        raise HTTPException(status_code=404, detail=f"Role '{role_id}' not found")
    allowed_levels = roles[role_id].get("data_access", [])
    return {
        "role_id": role_id,
        "classification": classification,
        "allowed": classification in allowed_levels,
        "role_data_access": allowed_levels,
    }
