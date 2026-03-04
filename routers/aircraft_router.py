from fastapi import APIRouter, HTTPException
from schemas.aircraft_schema import AircraftCreate, AircraftResponse, AircraftUpdate
from services.aircraft_service import AircraftService

router = APIRouter()

aircraft_service = AircraftService()


@router.get("/", response_model=list[AircraftResponse])
def get_all_aircraft() -> list[AircraftResponse]:
    aircraft_list = aircraft_service.get_all_aircraft()
    return [AircraftResponse.model_validate(aircraft) for aircraft in aircraft_list]


@router.get("/{aircraft_id}", response_model=AircraftResponse)
def get_aircraft(aircraft_id: int):
    aircraft = aircraft_service.get_aircraft_by_id(aircraft_id)
    if aircraft is None:
        raise HTTPException(status_code=404, detail="Aircraft not found")
    return aircraft


@router.post("/", response_model=AircraftResponse)
def create_aircraft(request: AircraftCreate):
    try:
        aircraft = aircraft_service.create_aircraft(
            tail_number=request.tail_number,
            model=request.model,
            manufacturer=request.manufacturer,
            year=request.year
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return aircraft


@router.put("/{aircraft_id}", response_model=AircraftResponse)
def update_aircraft(aircraft_id: int, request: AircraftUpdate):
    try:
        aircraft = aircraft_service.update_aircraft(
            aircraft_id=aircraft_id,
            tail_number=request.tail_number,
            model=request.model,
            manufacturer=request.manufacturer,
            year=request.year
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return aircraft


@router.delete("/{aircraft_id}")
def delete_aircraft(aircraft_id: int) -> dict[str, str | bool]:
    try:
        aircraft_service.delete_aircraft(aircraft_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return {"success": True, "message": "Aircraft deleted successfully"}
