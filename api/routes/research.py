import logging
from fastapi import APIRouter, Depends
import time
from api.schemas.research import ResearchRequest, ResearchResponse
from agents.graph import build_graph
from datetime import datetime, timezone
from api.middleware.auth import require_api_key
from api.middleware.rate_limit import rate_limit

from evals.policy import derive_verdict, normalize_scores

import logging

logger = logging.getLogger("atlas")

router = APIRouter(prefix="/research", tags=["research"])

graph = build_graph()

@router.post(
    "/run",
    response_model=ResearchResponse,
    dependencies=[
        Depends(require_api_key),
        Depends(rate_limit),
    ],
)
async def run_research(req: ResearchRequest):
    start_time = time.time()

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

    # Calculate and save latency
    latency_ms = int((time.time() - start_time) * 1000)
    metrics = result.get("metrics", {})
    metrics["latency_ms"] = latency_ms

    raw_scores = result.get("eval_scores", {})
    normalized_scores = normalize_scores(raw_scores)
    verdict = derive_verdict(normalized_scores)

    logger.info(
        {
            "topic": req.topic,
            "verdict": verdict,
            "latency_ms": latency_ms,
            "tokens_used": metrics.get("tokens_used"),
            "cost_usd": metrics.get("cost_usd"),
        }
    )

    return {
        "executive_summary": result.get("executive_summary"),
        "market_overview": result.get("market_overview"),
        "competitors": result.get("competitors"),
        "opportunities": result.get("opportunities"),
        "risks": result.get("risks"),

        # ← flatten for frontend
        "eval_scores": normalized_scores,
        "verdict": verdict,
        "latency": latency_ms,

        # optional (nice for future)
        "metrics": metrics,
    }

    # return {
    #     "executive_summary": result.get("executive_summary"),
    #     "market_overview": result.get("market_overview"),
    #     "competitors": result.get("competitors"),
    #     "opportunities": result.get("opportunities"),
    #     "risks": result.get("risks"),
    #     "eval": {
    #         "scores": raw_scores,
    #         "normalized_scores": normalized_scores,
    #         "verdict": verdict,
    #     },
    #     "metrics": metrics,
    # }


