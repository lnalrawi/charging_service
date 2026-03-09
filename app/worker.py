import requests
from app.queue_service import dequeue_request
from app.validator import is_valid_token
from app.storage import save_decision

AUTH_SERVICE_URL = "http://localhost:9000/authorize"
TIMEOUT = 3


def process_request(data):

    station_id = str(data["station_id"])
    token = data["driver_token"]
    callback = data["callback_url"]

    if not is_valid_token(token):
        status = "invalid"
    else:
        try:
            response = requests.post(
                AUTH_SERVICE_URL,
                json={
                    "station_id": station_id,
                    "driver_token": token
                },
                timeout=TIMEOUT
            )

            status = response.json().get("status", "unknown")

        except requests.Timeout:
            status = "unknown"

        except requests.RequestException:
            status = "unknown"

    result = {
        "station_id": station_id,
        "driver_token": token,
        "status": status
    }

    save_decision(station_id, token, status)

    try:
        requests.post(callback, json=result, timeout=5)
    except requests.RequestException:
        pass


def worker_loop():
    while True:
        data = dequeue_request()
        process_request(data)