from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from evals.policy import EvalVerdict


class ResearchRequest(BaseModel):
    topic: str


class EvalResult(BaseModel):
    scores: Dict[str, float]
    verdict: EvalVerdict


class ResearchResponse(BaseModel):
    executive_summary: Optional[str]
    market_overview: Optional[str]
    competitors: Optional[List[Dict[str, Any]]]
    opportunities: Optional[List[str]]
    risks: Optional[List[str]]
    eval: EvalResult
