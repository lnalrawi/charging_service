from fastapi.testclient import TestClient
from app.auth_service import app

client = TestClient(app)

def test_authorize_allowed():
    response = client.post("/authorize", json={
        "station_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "driver_token": "LaythAlRawi_05031986"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "allowed"

def test_authorize_not_allowed():
    response = client.post("/authorize", json={
        "station_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "driver_token": "invalidtoken123"
    })
    assert response.json()["status"] == "not_allowed"