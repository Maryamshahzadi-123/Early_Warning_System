class AircraftService:

    # def __init__(self):
    #     self.aircrafts = []
    def __init__(self):
       self.aircrafts = []
       self.scanning = True
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
