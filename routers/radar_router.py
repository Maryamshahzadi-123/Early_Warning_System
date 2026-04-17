from fastapi import APIRouter, HTTPException
from schemas.radar_schema import StartTrackingRequest, RadarMessage, StopTrackingRequest, DroneLocationResponse, UpdateLocationRequest
from services.radar_service import RadarService
from data_layer.repositories.drone_repository import DroneRepository

router = APIRouter()

drone_repository = DroneRepository()
radar_service = RadarService(drone_repository)

@router.post("/start", response_model=RadarMessage)
async def start_tracking(request: StartTrackingRequest) -> RadarMessage:
    success, message = await radar_service.radar_entry(request.drone_id)

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message

@router.post("/update-location", response_model=RadarMessage)
async def update_drone_location(request: UpdateLocationRequest) -> RadarMessage:
    success, message = await radar_service.update_drone_location(request.drone_id, request.latitude, request.longitude)

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message

@router.post("/stop", response_model=RadarMessage)
async def stop_tracking(request: StopTrackingRequest) -> RadarMessage:
    success, message = await radar_service.radar_exit(request.drone_id)

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message
