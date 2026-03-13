from pydantic import BaseModel
from typing import Optional


class RadarEntryRequest(BaseModel):
    drone_id: str
    timestamp: Optional[str] = None


class RadarMessage(BaseModel):
    message: str
    drone_id: str
