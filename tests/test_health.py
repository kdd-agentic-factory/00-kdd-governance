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


def test_metrics_endpoint(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200
