from entities.airspace import Airspace


class AircraftService:

    def __init__(self):
        self.aircrafts = []
        self.scanning = True
        self.airspace = Airspace()
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

    def process_aircraft(self, aircraft):
        self.detect(aircraft)
#F3 
    def detect(self, aircraft):
        if self.airspace.is_inside(aircraft["position"]):
            if aircraft["id"] not in self.detected:
                self.detected.append(aircraft["id"])
                status = self.recognize_aircraft(aircraft)
#F7
                print(f"  Aircraft {aircraft['id']} , Type: {aircraft['type'].upper()} , Status: {status}")
                if status == "UNKNOWN":
                    self.raise_alert(aircraft)

    
    def raise_alert(self, aircraft):
        #F8 (location ,speed)
         print(f"     ALERT: Unknown aircraft detected at position {aircraft['position']}  iD: {aircraft['id']}   DIRECTION:  {aircraft['direction']} at {aircraft['speed']} km/h")
         
        
# F4 + F6
    def recognize_aircraft(self, aircraft):
        if aircraft["id"] in self.friendly_ids:
            return "FRIENDLY"         # F4
        elif self.airspace.is_inside(aircraft["position"]):
            return "UNKNOWN"          # F6
        else:
            return "NOT FRIENDLY"     



        
        

        
       


      


