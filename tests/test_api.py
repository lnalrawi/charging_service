
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_start_session_endpoint():
    payload = {
        "station_id": "123e4567-e89b-12d3-a456-426614174000",
        "driver_token": "LaythAlRawi_05031986",
        "callback_url": "http://example.com/callback"
    }


    response = client.post("/start-session", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "accepted"
    assert "Request is being processed asynchronously" in data["message"]