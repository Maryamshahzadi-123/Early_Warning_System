from entities.airspace import airspace


class AircraftService:

    def __init__(self):
        self.aircrafts = []
        self.scanning = True
        self.airspace = airspace()
        self.detected = []
        self.friendly_ids = ["AC001", "AC003", "AC006", "AC008", "AC010"] #F4

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
                status = self.recognize_aircraft(aircraft)
                print(f"  Aircraft {aircraft['id']} , Type: {aircraft['type'].upper()} , Status: {status}")

#F4
    def recognize_aircraft(self, aircraft):
        if aircraft["id"] in self.friendly_ids:
            return "FRIENDLY"
        else:
            return "NOT FRIENDLY"