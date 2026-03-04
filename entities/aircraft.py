from pydantic import BaseModel
from typing import Optional


class Aircraft(BaseModel):
    id: int
    tail_number: str
    model: str
    manufacturer: str
    year: Optional[int] = None
