from data_layer.db_context import DbContext
from schemas.radar_schema import RadarMessage
from typing import Tuple


class RadarService:
    def radar_entry(self, drone_id: str, timestamp: str) -> Tuple[bool, RadarMessage]:
        entered_drones = DbContext.get_entered_drones()

        if drone_id in entered_drones:
            return False, RadarMessage(
                message=f"Drone {drone_id} is already in radar area",
                drone_id=drone_id
            )

        DbContext.add_entered_drone(drone_id)
        return True, RadarMessage(
            message=f"Drone {drone_id} entered radar area",
            drone_id=drone_id
        )
