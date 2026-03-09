from fastapi import FastAPI
from app.models import StartSessionRequest
from app.queue_service import enqueue_request
from app.worker import worker_loop
import threading
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    t = threading.Thread(target=worker_loop, daemon=True)
    t.start()
    yield


app = FastAPI(title="ChargePoint Async Session API", lifespan=lifespan)

@app.post("/start-session")
async def start_session(request: StartSessionRequest):
    """
    Start a charging session asynchronously.
    """
    # Enqueue the request for async processing
    enqueue_request(request.model_dump())

    # Immediate acknowledgment response
    return {
        "status": "accepted",
        "message": "Request is being processed asynchronously. "
                   "The result will be sent to the provided callback URL."
    }
