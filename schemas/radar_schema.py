from pydantic import BaseModel


class StartTrackingRequest(BaseModel):
    drone_id: str


class UpdateLocationRequest(BaseModel):
    drone_id: str
    latitude: float
    longitude: float


class RadarMessage(BaseModel):
    message: str
    drone_id: str


class StopTrackingRequest(BaseModel):
    drone_id: str


class DroneLocationResponse(BaseModel):
    drone_id: str
    latitude: float
    longitude: float
    status: str
    last_updated: str
