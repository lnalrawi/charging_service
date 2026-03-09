ChargePoint Async Charging Session API

Overview
This project is a small service that simulates how a charging station starts a charging session.
The system receives a request from a driver, checks if the driver is allowed to charge at the station, and sends the result to a callback URL.
The API accepts the request immediately and processes it in the background.

Architecture
The system contains these components:
1- API Layer (Receives the charging session request, Validates the input, Places the request into a queue, Returns an immediate response)

2- Queue (Stores requests temporarily, Allows asynchronous processing)

3- Worker (Reads requests from the queue, Validates the driver token, Calls the authorization service, Saves the decision in a database, Sends the result to the callback URL)

4- Authorization Service (Simple HTTP service, Uses an Access Control List (ACL), Returns:allowed OR not_allowed)

5- Database (SQLite database, Stores authorization decisions for debugging and auditing)

Request Flow
1- Driver sends a request to the API.

2- API validates the request.

3- API places the request in the queue.

4- API returns an accepted response immediately.

5- Worker reads the request from the queue.

6- Worker calls the authorization service.

7- The decision is stored in the database.

8- The result is sent to the callback URL.

API Endpoint
Start Charging Session

POST: /start-session
Request Example
{
  "station_id": "123e4567-e89b-12d3-a456-426614174000",
  "driver_token": "ValidDriverToken123456789",
  "callback_url": "http://localhost:8001/callback"
}
Response Example
{
  "status": "accepted",
  "message": "Request is being processed asynchronously. The result will be sent to the provided callback URL."
}


Callback Response
When processing finishes, the system sends the result to the callback URL.
Example:
{
  "station_id": "123e4567-e89b-12d3-a456-426614174000",
  "driver_token": "ValidDriverToken123456789",
  "status": "allowed"
}
Possible status values (allowed, not_allowed, unknown, invalid).


Running the Application

1- Install dependencies (pip install -r requirements.txt).

2- Start the Authorization Service (uvicorn app.auth_service:app --port 9000)

3- Start the Callback Server (for testing) (uvicorn app.callback_server:app --port 8001)

4- Start the Main API (uvicorn main:app --port 8000)



Running Tests:
To run the test suite (pytest tests/)
The tests check (API endpoint, Authorization service, Queue functionality, Token validation)

Notes

* The queue is implemented using Python's queue.Queue. I beleive this could be good option this time for simplicity to simulate asynchronous processing. but for production we could use distributed message broker such as Redis, RabbitMQ, or Kafka.
* SQLite is used for simple persistence.
* The worker runs in a background thread.
* If the authorization service does not respond within the timeout, the result will be unknown.
