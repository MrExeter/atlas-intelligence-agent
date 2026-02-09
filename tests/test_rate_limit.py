def test_rate_limit_exceeded(client, monkeypatch):
    monkeypatch.setenv("RATE_LIMIT_PER_MINUTE", "2")

    headers = {"X-API-Key": "test"}

    client.post("/research/run", headers=headers, json={"topic": "A"})
    client.post("/research/run", headers=headers, json={"topic": "B"})
    r = client.post("/research/run", headers=headers, json={"topic": "C"})

    assert r.status_code == 429


def test_rate_limit_allows_under_limit(client, monkeypatch):
    monkeypatch.setenv("RATE_LIMIT_PER_MINUTE", "5")

    headers = {"X-API-Key": "test"}

    r = client.post("/research/run", headers=headers, json={"topic": "OK"})
    assert r.status_code == 200
