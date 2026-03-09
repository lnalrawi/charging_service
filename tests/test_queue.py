from uuid import UUID
from app.queue_service import enqueue_request, dequeue_request, request_queue

def test_enqueue_dequeue():
    # Clear queue to remove leftover items from previous tests
    while not request_queue.empty():
        request_queue.get()

    data = {
        "station_id": UUID("123e4567-e89b-12d3-a456-426614174000"),
        "driver_token": "ABCDE12345ABCDE12345ABCDE",
        "callback_url": "http://example.com/callback"
    }
    enqueue_request(data)
    result = dequeue_request()
    assert result == data