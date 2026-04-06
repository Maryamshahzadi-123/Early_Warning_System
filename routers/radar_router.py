from fastapi import APIRouter, HTTPException
from schemas.radar_schema import RadarEntryRequest, RadarMessage, RadarExitRequest, RadarUpdateRequest
from services.radar_service import RadarService
from data_layer.db_context import DbContext

router = APIRouter()

db_context = DbContext()
radar_service = RadarService(db_context)

@router.post("/entry", response_model=RadarMessage)
async def radar_entry(request: RadarEntryRequest) -> RadarMessage:
    success, message = await radar_service.radar_entry(
        request.drone_id, request.latitude, request.longitude
    )

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message

@router.post("/exit", response_model=RadarMessage)
async def radar_exit(request: RadarExitRequest) -> RadarMessage:
    success, message = await radar_service.radar_exit(request.drone_id)

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message

@router.put("/update", response_model=RadarMessage)
async def radar_update(request: RadarUpdateRequest) -> RadarMessage:
    success, message = await radar_service.radar_update(
        request.drone_id, request.latitude, request.longitude
    )

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message