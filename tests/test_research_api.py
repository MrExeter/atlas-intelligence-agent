from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_research_run_contract():
    r = client.post("/research/run", json={"topic": "AI developer tools"})
    assert r.status_code == 200

    data = r.json()

    for key in [
        "executive_summary",
        "market_overview",
        "competitors",
        "opportunities",
        "risks",
        "eval_scores",
    ]:
        assert key in data
