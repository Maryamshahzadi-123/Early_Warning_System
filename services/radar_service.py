from data_layer.repositories.drone_repository import DroneRepository
from schemas.radar_schema import RadarMessage, DroneLocationResponse
from typing import Tuple, Optional
import threading


class RadarService:
    def __init__(self, drone_repository: DroneRepository):
        self.drone_repository = drone_repository
        self.background_tasks = {}

    async def radar_entry(self, drone_id: str) -> Tuple[bool, RadarMessage]:
        entered_drones = self.drone_repository.get_entered_drones()

        if drone_id in entered_drones:
            return False, RadarMessage(
                message=f"Drone {drone_id} is already in radar area",
                drone_id=drone_id
            )

        # Default starting coordinates (Lahore, Pakistan)
        default_latitude = 31.5204
        default_longitude = 74.3587

        self.drone_repository.add_entered_drone(drone_id, default_latitude, default_longitude)

        #for every 10-second updates
        self._start_background_update(drone_id)

        return True, RadarMessage(
            message=f"Drone {drone_id} entered radar area and tracking started",
            drone_id=drone_id
        )

    async def radar_exit(self, drone_id: str) -> Tuple[bool, RadarMessage]:
        entered_drones = self.drone_repository.get_entered_drones()
        if drone_id not in entered_drones:
            return False, RadarMessage(
               message=f"Drone {drone_id} is not in radar area",
               drone_id=drone_id
            )

        # Stop background task
        self._stop_background_update(drone_id)

        self.drone_repository.remove_entered_drone(drone_id)
        return True, RadarMessage(
            message=f"Drone {drone_id} exited radar area and tracking stopped",
            drone_id=drone_id
        )

    def get_drone_location(self, drone_id: str) -> Optional[DroneLocationResponse]:
        drone_info = self.drone_repository.get_drone_info(drone_id)

        if drone_info is None:
            return None

        return DroneLocationResponse(
            drone_id=drone_id,
            latitude=drone_info["latitude"],
            longitude=drone_info["longitude"],
            status=drone_info["status"],
            last_updated=drone_info["last_updated"].isoformat()
        )

    async def update_drone_location(self, drone_id: str, latitude: float, longitude: float) -> Tuple[bool, RadarMessage]:
        entered_drones = self.drone_repository.get_entered_drones()

        if drone_id not in entered_drones:
            return False, RadarMessage(
                message=f"Drone {drone_id} is not in radar area",
                drone_id=drone_id
            )

        self.drone_repository.manual_update_location(drone_id, latitude, longitude)

        return True, RadarMessage(
            message=f"Drone {drone_id} location updated successfully",
            drone_id=drone_id
        )

    def _start_background_update(self, drone_id: str):
        stop_event = threading.Event()
        self.background_tasks[drone_id] = stop_event

        def update_loop():
            while not stop_event.is_set():
                stop_event.wait(10)  # Wait 10 seconds
                if not stop_event.is_set():
                    self.drone_repository.update_drone_location(drone_id)

        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()

    def _stop_background_update(self, drone_id: str):
        if drone_id in self.background_tasks:
            self.background_tasks[drone_id].set()
            del self.background_tasks[drone_id]
