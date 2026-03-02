from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.aircraft_services import AircraftService
from entities.aircraft import Aircraft

app = FastAPI()

aircraft_service = AircraftService()
aircraft_db = {}

# Request Model
class AircraftCreate(BaseModel):
    id: str
    x: float
    y: float
    aircraft_type: str
    speed: float
    direction: str


# Get All Aircraft
@app.get("/aircraft")
def get_all_aircraft():
    return list(aircraft_db.values())


# Get Aircraft By ID
@app.get("/aircraft/{aircraft_id}")
def get_aircraft(aircraft_id: str):
    if aircraft_id not in aircraft_db:
        raise HTTPException(status_code=404, detail="Aircraft not found")

    return aircraft_db[aircraft_id]


# Create Aircraft
@app.post("/aircraft")
def add_aircraft(data: AircraftCreate):

    if data.id in aircraft_db:
        raise HTTPException(status_code=400, detail="Aircraft already exists")

    # Create object
    new_aircraft = Aircraft(
        data.id,
        data.x,
        data.y,
        data.aircraft_type,
        data.speed,
        data.direction
    )

    aircraft_dict = new_aircraft.to_dict()

    # Save in local database
    aircraft_db[data.id] = aircraft_dict

    # Optional: send to service layer if needed
    aircraft_service.process_aircraft(aircraft_dict)

    return aircraft_dict