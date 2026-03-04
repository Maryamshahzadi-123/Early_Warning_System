from pydantic import BaseModel
from typing import Optional


class AircraftCreate(BaseModel):
    tail_number: str
    model: str
    manufacturer: str
    year: Optional[int] = None


class AircraftResponse(BaseModel):
    id: int
    tail_number: str
    model: str
    manufacturer: str
    year: Optional[int] = None


class AircraftUpdate(BaseModel):
    tail_number: Optional[str] = None
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    year: Optional[int] = None
