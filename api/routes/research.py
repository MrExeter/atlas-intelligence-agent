from fastapi import APIRouter
from api.schemas.research import ResearchRequest, ResearchResponse
from agents.graph import build_graph
from datetime import datetime, timezone

router = APIRouter(prefix="/research", tags=["research"])

graph = build_graph()


@router.post("/run", response_model=ResearchResponse)
def run_research(req: ResearchRequest):
    initial_state = {
        "topic": req.topic,
        "raw_documents": [],
        "retrieved_chunks": [],
        "started_at": datetime.now(timezone.utc),
        "metrics": {
            "tokens_used": 0,
            "latency_ms": 0.0,
            "cost_usd": 0.0
        }
    }

    result = graph.invoke(initial_state)

    return {
        "executive_summary": result.get("executive_summary"),
        "market_overview": result.get("market_overview"),
        "competitors": result.get("competitors"),
        "opportunities": result.get("opportunities"),
        "risks": result.get("risks"),
        "eval_scores": result.get("eval_scores"),
    }
