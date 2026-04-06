from data_layer.db_context import DbContext
from schemas.radar_schema import RadarMessage
from typing import Tuple


class RadarService:
    def __init__(self, db_context: DbContext):
        self.db_context = db_context

    async def radar_entry(self, drone_id: str, latitude: float, longitude: float) -> Tuple[bool, RadarMessage]:
        entered_drones = self.db_context.get_entered_drones()

        if drone_id in entered_drones:
            return False, RadarMessage(
                message=f"Drone {drone_id} is already in radar area",
                drone_id=drone_id
            )

        self.db_context.add_entered_drone(drone_id, latitude, longitude)
        return True, RadarMessage(
            message=f"Drone {drone_id} entered radar area",
            drone_id=drone_id
        )


    async def radar_exit(self, drone_id: str) -> Tuple[bool, RadarMessage]:
        entered_drones = self.db_context.get_entered_drones()
        if drone_id not in entered_drones:
            return False, RadarMessage(
               message=f"Drone {drone_id} is not in radar area",
               drone_id=drone_id
            )
        self.db_context.remove_entered_drone(drone_id)
        return True, RadarMessage(
            message=f"Drone {drone_id} exited radar area",
            drone_id=drone_id
        )

    async def radar_update(self, drone_id: str, latitude: float, longitude: float) -> Tuple[bool, RadarMessage]:
        entered_drones = self.db_context.get_entered_drones()
        
        if drone_id not in entered_drones:
            return False, RadarMessage(
                message=f"Drone {drone_id} is not in radar area",
                drone_id=drone_id
            )
        
        self.db_context.update_drone_position(drone_id, latitude, longitude)
        return True, RadarMessage(
            message=f"Drone {drone_id} position updated to ({latitude}, {longitude})",
            drone_id=drone_id
        )