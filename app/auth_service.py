from fastapi import FastAPI

app = FastAPI()

ACL = {
    "3fa85f64-5717-4562-b3fc-2c963f66afa6": [
        "LaythAlRawi_05031986"
    ]
}

@app.post("/authorize")
def authorize(data: dict):

    station = data["station_id"]
    token = data["driver_token"]

    allowed_tokens = ACL.get(station, [])

    if token in allowed_tokens:
        return {"status": "allowed"}

    return {"status": "not_allowed"}