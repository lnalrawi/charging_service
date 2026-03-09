# callback_server.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/callback")
async def callback(request: Request):
    data = await request.json()
    print("Callback received:", data)
    return {"status": "ok"}