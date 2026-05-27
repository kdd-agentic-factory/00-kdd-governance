"""Tests for API key authentication on protected governance routes."""
import pytest
from fastapi.testclient import TestClient

from kdd_governance.main import app
import kdd_governance.security as _sec


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_open_when_no_key_configured(client):
    """With KDD_INTERNAL_API_KEY unset (dev mode) all routes are open."""
    resp = client.get("/api/v1/kdd/stages")
    assert resp.status_code == 200


def test_enforce_key_when_configured(client, monkeypatch):
    monkeypatch.setattr(_sec, "_API_KEY", "super-secret-key")
    resp = client.get("/api/v1/kdd/stages")
    assert resp.status_code == 401


def test_valid_key_passes(client, monkeypatch):
    monkeypatch.setattr(_sec, "_API_KEY", "super-secret-key")
    resp = client.get("/api/v1/kdd/stages", headers={"X-API-Key": "super-secret-key"})
    assert resp.status_code == 200


def test_wrong_key_rejected(client, monkeypatch):
    monkeypatch.setattr(_sec, "_API_KEY", "super-secret-key")
    resp = client.get("/api/v1/kdd/stages", headers={"X-API-Key": "wrong-key"})
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid or missing X-API-Key header"
