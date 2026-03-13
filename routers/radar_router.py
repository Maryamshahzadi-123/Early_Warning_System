from fastapi import APIRouter, HTTPException
from schemas.radar_schema import RadarEntryRequest, RadarMessage
from services.radar_service import RadarService
from datetime import datetime

router = APIRouter()
radar_service = RadarService()


@router.post("/entry", response_model=RadarMessage)
def radar_entry(request: RadarEntryRequest) -> RadarMessage:
    timestamp = request.timestamp or datetime.now().isoformat()
    success, message = radar_service.radar_entry(request.drone_id, timestamp)

    if not success:
        raise HTTPException(status_code=400, detail=message.message)

    return message
