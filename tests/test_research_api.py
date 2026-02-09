from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_research_run_contract(client, monkeypatch):
    monkeypatch.setenv("ATLAS_API_KEY", "test")
    r = client.post(
        "/research/run",
        headers={"X-API-Key": "test"},
        json={"topic": "AI developer tools"},
    )
    assert r.status_code == 200
