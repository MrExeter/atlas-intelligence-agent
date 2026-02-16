from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from evals.policy import EvalVerdict


class ResearchRequest(BaseModel):
    topic: str


class ResearchResponse(BaseModel):
    executive_summary: Optional[str]
    market_overview: Optional[str]
    competitors: Optional[List[Dict[str, Any]]]
    opportunities: Optional[List[str]]
    risks: Optional[List[str]]

    # flattened evaluation fields
    eval_scores: Optional[Dict[str, float]]
    verdict: Optional[EvalVerdict]

    # performance metadata
    latency: Optional[int]

    # keep for future extensibility
    metrics: Optional[Dict[str, Any]]
