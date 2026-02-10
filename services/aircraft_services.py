from entities.airspace import airspace


class AircraftService:

    def __init__(self):
        self.aircrafts = []
        self.scanning = True
        self.airspace = airspace()
        self.detected = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def identify_aircraft(self, aircraft_id):
        for ac in self.aircrafts:
            if ac.aircraft_id == aircraft_id:
                if getattr(ac, "friendly", True):
                    return "Friendly"
                return "Unknown"
        return "Not Found"

    def track_aircraft(self, aircraft_id):
        for ac in self.aircrafts:
            if ac.aircraft_id == aircraft_id:
                return ac.position, getattr(ac, "movement", None)
        return None


#F3
    def detect(self, aircraft):
        if self.airspace.is_inside(aircraft["position"]):
            if aircraft["id"] not in self.detected:
                self.detected.append(aircraft["id"])
                print(f"Aircraft {aircraft['id']} ({aircraft['type']})  Entered Airspace")

           
           
