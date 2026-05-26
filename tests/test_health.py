"""Tests for the governance-policy-service health and metrics endpoints."""
import pytest
from fastapi.testclient import TestClient

from kdd_governance.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_health_returns_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["service"] == "governance-policy-service"
    assert "version" in data
    assert "environment" in data


def test_health_shape(client):
    resp = client.get("/health")
    data = resp.json()
    assert set(data.keys()) >= {"status", "service", "version", "environment"}


def test_metrics_endpoint_returns_prometheus_format(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "text/plain" in resp.headers["content-type"]
    assert b"governance_http_requests_total" in resp.content


def test_metrics_records_validation_counter(client):
    client.post("/kdd/validate-artifact", json={
        "artifact_id": "art-metrics-test",
        "artifact_type": "dataset",
        "kdd_stage": "selection",
        "source_repository": "github.com/kdd/test",
    })
    resp = client.get("/metrics")
    assert b"governance_validations_total" in resp.content
