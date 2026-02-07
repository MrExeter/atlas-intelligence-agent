from pydantic import BaseModel
from typing import Any, Dict, List, Optional


class ResearchRequest(BaseModel):
    topic: str


class ResearchResponse(BaseModel):
    executive_summary: Optional[str]
    market_overview: Optional[str]
    competitors: Optional[List[Dict[str, Any]]]
    opportunities: Optional[List[str]]
    risks: Optional[List[str]]
    eval_scores: Optional[Dict[str, float]]
