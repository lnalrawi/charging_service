from pydantic import BaseModel, HttpUrl
from uuid import UUID

class StartSessionRequest(BaseModel):
    station_id: UUID
    driver_token: str
    callback_url: HttpUrl