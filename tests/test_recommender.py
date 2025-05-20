import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recommend_returns_results():
    response = client.post("/recommend", json={"text": "FastAPI moderno", "top_k": 2})
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert len(data["recommendations"]) == 2
    for rec in data["recommendations"]:
        assert "id" in rec
        assert "title" in rec
        assert "score" in rec