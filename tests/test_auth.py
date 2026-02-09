def test_missing_api_key(client):
    resp = client.post("/research/run", json={"topic": "AI tools"})
    assert resp.status_code == 401


def test_invalid_api_key(client, monkeypatch):
    monkeypatch.setenv("ATLAS_API_KEY", "correct")
    resp = client.post(
        "/research/run",
        headers={"X-API-Key": "wrong"},
        json={"topic": "AI tools"},
    )
    assert resp.status_code == 401


def test_valid_api_key(client, monkeypatch):
    monkeypatch.setenv("ATLAS_API_KEY", "correct")
    resp = client.post(
        "/research/run",
        headers={"X-API-Key": "correct"},
        json={"topic": "AI tools"},
    )
    assert resp.status_code == 200
