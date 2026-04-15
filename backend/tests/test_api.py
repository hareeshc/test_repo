from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_overview_metrics() -> None:
    response = client.get("/api/v1/metrics/overview")
    assert response.status_code == 200
    payload = response.json()
    assert "activation_rate" in payload
    assert "impact_positive_response_rate" in payload
