from pydantic import BaseModel, Field


class RadarEntryRequest(BaseModel):
    drone_id: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class RadarMessage(BaseModel):
    message: str
    drone_id: str


class RadarExitRequest(BaseModel):
    drone_id: str


class RadarUpdateRequest(BaseModel):
    drone_id: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)