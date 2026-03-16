from fastapi import APIRouter, HTTPException
from schemas.radar_schema import RadarEntryRequest, RadarMessage
from services.radar_service import RadarService
from data_layer.db_context import DbContext
from datetime import datetime

router = APIRouter()

db_context = DbContext()
radar_service = RadarService(db_context)


@router.post("/entry", response_model=RadarMessage)
async def radar_entry(request: RadarEntryRequest) -> RadarMessage:
    timestamp = request.timestamp or datetime.now().isoformat()
    success, message = await radar_service.radar_entry(request.drone_id, timestamp)

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message
