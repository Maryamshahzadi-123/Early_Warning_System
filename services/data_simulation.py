from services.aircraft_services import AircraftService

class DataSimulation:
    def __init__(self, aircraft_service=None):
        if aircraft_service is None:
            aircraft_service = AircraftService()
        self.aircraft_service = aircraft_service

        #dummy data (10 aircraft)
        self.aircraft_data = [
            {"id": "AC001",    "position": {"x": 10, "y": 20},    "type": "commercial",  "speed": 300,  "direction": "North"  },
            {"id": "AC002",    "position": {"x": 120, "y": 80},   "type": "military",    "speed": 250,  "direction": "East"   },
            {"id": "AC003",    "position": {"x": 50, "y": 60},    "type": "commercial",  "speed": 190,  "direction": "south"  },
            {"id": "AC004",    "position": {"x": -10, "y": 40},   "type": "military",    "speed": 200,  "direction": "west"   },
            {"id": "AC005",    "position": {"x": 90, "y": 110},   "type": "commercial",  "speed":280,   "direction": "North"   },
            {"id": "AC006",    "position": {"x": 30, "y": 25},    "type": "military",    "speed":140,   "direction": "North"   },
            {"id": "AC007",    "position": {"x": 200, "y": 150},  "type": "commercial",  "speed":240,   "direction": "East"   },
            {"id": "AC008",    "position": {"x": 70, "y": 40},    "type": "commercial",  "speed":290,   "direction": "North"   },
            {"id": "AC009",    "position": {"x": 15, "y": 95},    "type": "military",    "speed":310,   "direction": "west"   },
            {"id": "AC010",    "position": {"x": 0, "y": 0},      "type": "military",    "speed":360,   "direction": "west"   },
        ]

    def run(self):
        for aircraft in self.aircraft_data:
            self.aircraft_service.process_aircraft(aircraft)
            
         
         
         
        
           
            
            
           
   
            