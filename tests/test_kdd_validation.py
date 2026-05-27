"""Tests for KDD artifact validation, evidence packets, and traceability endpoints."""
import pytest
from fastapi.testclient import TestClient

from kdd_governance.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


# ── /kdd/stages ───────────────────────────────────────────────────────────────

def test_list_stages(client):
    resp = client.get("/api/v1/kdd/stages")
    assert resp.status_code == 200
    stages = resp.json()["stages"]
    assert len(stages) == 6
    ids = [s["stage_id"] for s in stages]
    assert "selection" in ids
    assert "deployment" in ids


def test_stages_are_ordered(client):
    stages = client.get("/api/v1/kdd/stages").json()["stages"]
    orders = [s["order"] for s in stages]
    assert orders == sorted(orders)


# ── /kdd/artifact-types ───────────────────────────────────────────────────────

def test_list_artifact_types(client):
    resp = client.get("/api/v1/kdd/artifact-types")
    assert resp.status_code == 200
    types = resp.json()["artifact_types"]
    assert "dataset" in types
    assert "pattern" in types
    assert "evidence_packet" in types


# ── /kdd/evidence-requirements ───────────────────────────────────────────────

def test_evidence_requirements(client):
    resp = client.get("/api/v1/kdd/evidence-requirements")
    assert resp.status_code == 200
    reqs = resp.json()["requirements"]
    assert "pattern" in reqs
    assert "source_session_id" in reqs["pattern"]


# ── /kdd/traceability-rules ───────────────────────────────────────────────────

def test_traceability_rules(client):
    resp = client.get("/api/v1/kdd/traceability-rules")
    assert resp.status_code == 200
    rules = resp.json()["rules"]
    assert len(rules) > 0


# ── /kdd/validate-artifact ────────────────────────────────────────────────────

def test_validate_valid_artifact(client):
    payload = {
        "artifact_id": "art-001",
        "artifact_type": "dataset",
        "kdd_stage": "selection",
        "source_repository": "github.com/kdd/datasets",
        "evidence": [],
        "metadata": {},
    }
    resp = client.post("/api/v1/kdd/validate-artifact", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is True
    assert data["traceability_score"] > 0.0
    assert data["missing_fields"] == []


def test_validate_artifact_missing_source_repo(client):
    payload = {
        "artifact_id": "art-002",
        "artifact_type": "dataset",
        "kdd_stage": "selection",
    }
    resp = client.post("/api/v1/kdd/validate-artifact", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is False
    assert "source_repository" in data["missing_fields"]
    assert data["traceability_score"] < 1.0


def test_validate_artifact_unknown_type(client):
    payload = {
        "artifact_id": "art-003",
        "artifact_type": "unknown_thing",
        "kdd_stage": "selection",
        "source_repository": "github.com/kdd",
    }
    resp = client.post("/api/v1/kdd/validate-artifact", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is False
    assert any("unknown_thing" in f for f in data["missing_fields"])


def test_validate_pattern_without_dataset_id(client):
    payload = {
        "artifact_id": "pat-001",
        "artifact_type": "pattern",
        "kdd_stage": "mining",
        "source_repository": "github.com/kdd",
        "evidence": [],
        "metadata": {},
    }
    resp = client.post("/api/v1/kdd/validate-artifact", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "dataset_id" in data["missing_fields"]


def test_validate_pattern_with_required_evidence(client):
    payload = {
        "artifact_id": "pat-002",
        "artifact_type": "pattern",
        "kdd_stage": "mining",
        "source_repository": "github.com/kdd",
        "evidence": ["source_session_id", "feature_ids", "kdd_stage"],
        "dataset_id": "ds-001",
        "metadata": {},
    }
    resp = client.post("/api/v1/kdd/validate-artifact", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is True


# ── /kdd/validate-evidence-packet ────────────────────────────────────────────

def test_validate_evidence_packet_complete(client):
    payload = {
        "evidence_packet_id": "ep-001",
        "claim": "Setup change reduces spin ratio at turn 3",
        "sources": [
            {"session_id": "s1", "type": "telemetry"},
            {"session_id": "s2", "type": "simulation"},
            {"session_id": "s3", "type": "historical"},
        ],
        "kdd_stages_covered": ["selection", "preprocessing", "transformation", "mining", "interpretation"],
    }
    resp = client.post("/api/v1/kdd/validate-evidence-packet", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is True
    assert data["completeness_score"] > 0.5
    assert data["groundedness_score"] > 0.0


def test_validate_evidence_packet_empty_sources(client):
    payload = {
        "evidence_packet_id": "ep-002",
        "claim": "Claim without evidence",
        "sources": [],
        "kdd_stages_covered": ["selection"],
    }
    resp = client.post("/api/v1/kdd/validate-evidence-packet", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is False


# ── /kdd/validate-dataset-lineage ────────────────────────────────────────────

def test_validate_dataset_lineage_complete(client):
    payload = {
        "dataset_id": "ds-001",
        "pipeline_id": "pipe-001",
        "feature_ids": ["f1", "f2"],
        "pattern_ids": ["p1"],
        "evidence_ids": ["e1"],
    }
    resp = client.post("/api/v1/kdd/validate-dataset-lineage", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["lineage_complete"] is True
    assert data["traceability_score"] == 0.95


def test_validate_dataset_lineage_incomplete(client):
    payload = {"dataset_id": "ds-002"}
    resp = client.post("/api/v1/kdd/validate-dataset-lineage", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["lineage_complete"] is False
    assert data["traceability_score"] == 0.5


# ── /kdd/validate-workflow-trace ─────────────────────────────────────────────

def test_validate_workflow_trace_complete(client):
    payload = {
        "workflow_id": "wf-001",
        "steps_completed": ["s1", "s2", "s3"],
        "artifacts_produced": ["a1", "a2"],
        "kdd_stages_covered": ["selection", "preprocessing", "mining"],
    }
    resp = client.post("/api/v1/kdd/validate-workflow-trace", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is True
    assert data["missing_required_stages"] == []


def test_validate_workflow_trace_missing_stage(client):
    payload = {
        "workflow_id": "wf-002",
        "steps_completed": ["s1"],
        "artifacts_produced": [],
        "kdd_stages_covered": ["selection"],
    }
    resp = client.post("/api/v1/kdd/validate-workflow-trace", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["valid"] is False
    assert len(data["missing_required_stages"]) > 0
