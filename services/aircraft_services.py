class AircraftService:
    def __init__(self):
        self.aircrafts =[]
    def add_aircraft(self,aircraft):
            self.aircrafts.append(aircraft)
    def identify_aircraft(self,aircraft_id):
        for ac in self.aircrafts:
            if ac.aircraft_id == aircraft_id:         
                return "Friendly" if getattr(ac,"friendly",True) else"Unknown"
        return"Not Found"
    def track_aircraft(self,aircraft_id):
        for ac in self.aircrafts:
            if ac.aircraft_id==aircraft_id:
                return getattr(ac,"position",None),getattr(ac,"movement",None)
        return None