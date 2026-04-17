from typing import Optional, Dict
from datetime import datetime
import random


class DroneRepository:
    _entered_drones: Dict[str, dict] = {}

    def get_entered_drones(self) -> set[str]:
        return set(DroneRepository._entered_drones.keys())

    def add_entered_drone(self, drone_id: str, latitude: float, longitude: float):
        DroneRepository._entered_drones[drone_id] = {
            "status": "active",
            "latitude": latitude,
            "longitude": longitude,
            "last_updated": datetime.utcnow()
        }

    def remove_entered_drone(self, drone_id: str):
        DroneRepository._entered_drones.pop(drone_id, None)

    def update_drone_location(self, drone_id: str) -> bool:
        if drone_id not in DroneRepository._entered_drones:
            return False

        # Random movement: ±0.001 degrees (approximately 100 meters)
        current = DroneRepository._entered_drones[drone_id]
        new_lat = current["latitude"] + random.uniform(-0.001, 0.001)
        new_lon = current["longitude"] + random.uniform(-0.001, 0.001)

        DroneRepository._entered_drones[drone_id]["status"] = "active"
        DroneRepository._entered_drones[drone_id]["latitude"] = new_lat
        DroneRepository._entered_drones[drone_id]["longitude"] = new_lon
        DroneRepository._entered_drones[drone_id]["last_updated"] = datetime.utcnow()
        return True

    def get_drone_info(self, drone_id: str) -> Optional[dict]:
        return DroneRepository._entered_drones.get(drone_id)

    def manual_update_location(self, drone_id: str, latitude: float, longitude: float):
        if drone_id in DroneRepository._entered_drones:
            DroneRepository._entered_drones[drone_id]["latitude"] = latitude
            DroneRepository._entered_drones[drone_id]["longitude"] = longitude
            DroneRepository._entered_drones[drone_id]["last_updated"] = datetime.utcnow()
