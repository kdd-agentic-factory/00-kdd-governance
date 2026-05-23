"""KDD governance validation endpoints."""
from typing import Any, Dict, List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# ── KDD Stage definitions ──────────────────────────────────────────────────────

_KDD_STAGES = [
    {"stage_id": "selection", "name": "Data Selection", "order": 1, "description": "Select relevant data sources and datasets"},
    {"stage_id": "preprocessing", "name": "Preprocessing", "order": 2, "description": "Clean, normalize and deduplicate data"},
    {"stage_id": "transformation", "name": "Transformation", "order": 3, "description": "Feature extraction and embedding creation"},
    {"stage_id": "mining", "name": "Pattern Mining", "order": 4, "description": "Discover patterns, clusters and anomalies"},
    {"stage_id": "interpretation", "name": "Interpretation & Evaluation", "order": 5, "description": "Build evidence packets and validate findings"},
    {"stage_id": "deployment", "name": "Knowledge Deployment", "order": 6, "description": "Apply knowledge to decisions and reports"},
]

_ARTIFACT_TYPES = [
    "dataset", "session", "telemetry_window", "feature_vector",
    "pattern", "evidence_packet", "model", "skill", "autoskill",
    "crew_chief_report", "setup_change_request", "simulation_result",
    "paper_section", "experiment_result", "adr",
]

_EVIDENCE_REQUIREMENTS = {
    "pattern": ["source_session_id", "feature_ids", "kdd_stage"],
    "setup_change_request": ["pattern_ids", "simulation_result_id", "evidence_packet_id"],
    "paper_section": ["experiment_ids", "evidence_packet_ids", "source_repository"],
    "crew_chief_report": ["session_id", "pattern_ids", "evidence_packet_id"],
}


class ArtifactValidationRequest(BaseModel):
    artifact_id: str
    artifact_type: str
    kdd_stage: str
    dataset_id: Optional[str] = None
    source_repository: Optional[str] = None
    evidence: List[str] = []
    metadata: Dict[str, Any] = {}


class ArtifactValidationResult(BaseModel):
    valid: bool
    traceability_score: float
    missing_fields: List[str]
    recommendations: List[str]


class EvidencePacketValidationRequest(BaseModel):
    evidence_packet_id: str
    claim: str
    sources: List[Dict[str, Any]]
    kdd_stages_covered: List[str]


class EvidencePacketValidationResult(BaseModel):
    valid: bool
    completeness_score: float
    missing_stages: List[str]
    groundedness_score: float
    recommendations: List[str]


class DatasetLineageRequest(BaseModel):
    dataset_id: str
    pipeline_id: Optional[str] = None
    feature_ids: List[str] = []
    pattern_ids: List[str] = []
    evidence_ids: List[str] = []


class WorkflowTraceRequest(BaseModel):
    workflow_id: str
    steps_completed: List[str]
    artifacts_produced: List[str]
    kdd_stages_covered: List[str]


# ── Endpoints ─────────────────────────────────────────────────────────────────

@router.get("/stages")
async def get_kdd_stages():
    return {"stages": _KDD_STAGES}


@router.get("/artifact-types")
async def get_artifact_types():
    return {"artifact_types": _ARTIFACT_TYPES}


@router.get("/evidence-requirements")
async def get_evidence_requirements():
    return {"requirements": _EVIDENCE_REQUIREMENTS}


@router.get("/traceability-rules")
async def get_traceability_rules():
    return {
        "rules": [
            "Every artifact must reference a KDD stage",
            "Every pattern must trace to a dataset session",
            "Every recommendation must reference evidence",
            "Every paper artifact must reference experiment results",
            "All tool calls must be audited via MCP Gateway",
        ]
    }


@router.post("/validate-artifact", response_model=ArtifactValidationResult)
async def validate_artifact(request: ArtifactValidationRequest):
    missing = []
    score = 1.0
    recommendations = []

    if request.artifact_type not in _ARTIFACT_TYPES:
        missing.append(f"unknown artifact_type '{request.artifact_type}'")
        score -= 0.3

    if not request.dataset_id and request.artifact_type in ("pattern", "feature_vector", "telemetry_window"):
        missing.append("dataset_id")
        score -= 0.2

    if not request.source_repository:
        missing.append("source_repository")
        score -= 0.1
        recommendations.append("Add source_repository for full KDD traceability")

    required_evidence = _EVIDENCE_REQUIREMENTS.get(request.artifact_type, [])
    provided_keys = set(request.metadata.keys()) | set(request.evidence)
    for req_field in required_evidence:
        if req_field not in provided_keys:
            missing.append(req_field)
            score -= 0.1

    return ArtifactValidationResult(
        valid=len(missing) == 0,
        traceability_score=max(0.0, round(score, 2)),
        missing_fields=missing,
        recommendations=recommendations,
    )


@router.post("/validate-evidence-packet", response_model=EvidencePacketValidationResult)
async def validate_evidence_packet(request: EvidencePacketValidationRequest):
    all_stages = {s["stage_id"] for s in _KDD_STAGES}
    covered = set(request.kdd_stages_covered)
    missing_stages = list(all_stages - covered - {"deployment"})

    completeness = len(covered) / (len(all_stages) - 1)
    groundedness = min(1.0, len(request.sources) * 0.2)

    return EvidencePacketValidationResult(
        valid=len(request.sources) >= 1 and completeness >= 0.5,
        completeness_score=round(completeness, 2),
        missing_stages=missing_stages,
        groundedness_score=round(groundedness, 2),
        recommendations=["Add more sources for higher groundedness"] if groundedness < 0.6 else [],
    )


@router.post("/validate-dataset-lineage")
async def validate_dataset_lineage(request: DatasetLineageRequest):
    complete = bool(request.dataset_id and request.pipeline_id and request.feature_ids and request.pattern_ids)
    return {
        "dataset_id": request.dataset_id,
        "lineage_complete": complete,
        "traceability_score": 0.95 if complete else 0.5,
        "chain": {
            "dataset": request.dataset_id,
            "pipeline": request.pipeline_id,
            "features": request.feature_ids,
            "patterns": request.pattern_ids,
            "evidence": request.evidence_ids,
        },
    }


@router.post("/validate-workflow-trace")
async def validate_workflow_trace(request: WorkflowTraceRequest):
    required_stages = {"selection", "preprocessing", "mining"}
    covered = set(request.kdd_stages_covered)
    missing = list(required_stages - covered)
    return {
        "workflow_id": request.workflow_id,
        "valid": len(missing) == 0,
        "kdd_stages_covered": request.kdd_stages_covered,
        "missing_required_stages": missing,
        "steps_completed": len(request.steps_completed),
        "artifacts_produced": len(request.artifacts_produced),
    }
