from services.aircraft_services import AircraftService

class DataSimulation:
    def __init__(self):
        self.aircraft_service = AircraftService()

        #dummy data (10 aircraft)
        self.aircraft_data = [
            {"id": "AC001",    "position": {"x": 10, "y": 20},    "type": "commercial"},
            {"id": "AC002",    "position": {"x": 120, "y": 80},   "type": "military"},
            {"id": "AC003",    "position": {"x": 50, "y": 60},    "type": "commercial"},
            {"id": "AC004",    "position": {"x": -10, "y": 40},   "type": "military"},
            {"id": "AC005",    "position": {"x": 90, "y": 110},   "type": "commercial"},
            {"id": "AC006",    "position": {"x": 30, "y": 25},    "type": "military"},
            {"id": "AC007",    "position": {"x": 200, "y": 150},  "type": "commercial"},
            {"id": "AC008",    "position": {"x": 70, "y": 40},    "type": "commercial"},
            {"id": "AC009",    "position": {"x": 15, "y": 95},    "type": "military"},
            {"id": "AC010",    "position": {"x": 0, "y": 0},      "type": "military"},
        ]

    def run(self):
        for aircraft in self.aircraft_data:
            self.aircraft_service.detect(aircraft)
