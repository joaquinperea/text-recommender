from typing import Dict, Any
from fastapi import APIRouter
from pydantic import BaseModel
from app.recommender import recommender

router = APIRouter()

class RecommendRequest(BaseModel):
    """Request model for the recommendation endpoint."""
    text: str
    top_k: int = 5

@router.post("/recommend", response_model=Dict[str, Any])
def recommend(req: RecommendRequest) -> Dict[str, Any]:
    """Endpoint to get article recommendations based on a query."""
    results = recommender.recommend(req.text, req.top_k)
    return {"recommendations": results}
