from entities.airspace import Airspace


class AircraftService:

    def __init__(self):
        self.airspace = Airspace()
        self.detected = []
        self.friendly_ids = ["AC001", "AC003", "AC006", "AC008", "AC010"]

    def process_aircraft(self, aircraft):
        self.detect(aircraft)

    def detect(self, aircraft):
        if self.airspace.is_inside(aircraft["position"]):
            if aircraft["id"] not in self.detected:
                self.detected.append(aircraft["id"])
            status = self.recognize_aircraft(aircraft)
            print(f"  Aircraft {aircraft['id']} , Type: {aircraft['type'].upper()} , Status: {status} , Position: ({aircraft['position']['x']}, {aircraft['position']['y']}) , Direction: {aircraft['direction']}")
            if status == "Unknown":
                self.raise_alert(aircraft)

    def raise_alert(self, aircraft):
        print(f"     ALERT: Unknown aircraft detected at position ({aircraft['position']['x']}, {aircraft['position']['y']})  iD: {aircraft['id']}   DIRECTION:  {aircraft['direction']} at {aircraft['speed']}")

    def update_position(self, aircraft_data, aircraft_id, new_x, new_y):
        for aircraft in aircraft_data:
            if aircraft["id"] == aircraft_id:
                old_x = aircraft["position"]["x"]
                old_y = aircraft["position"]["y"]
                dx = new_x - old_x
                dy = new_y - old_y
                if dx > 0 and dy > 0:
                    new_direction = "North-East"
                elif dx < 0 and dy > 0:
                    new_direction = "North-West"
                elif dx > 0 and dy < 0:
                    new_direction = "South-East"
                elif dx < 0 and dy < 0:
                    new_direction = "South-West"
                elif dx > 0:
                    new_direction = "East"
                elif dx < 0:
                    new_direction = "West"
                elif dy > 0:
                    new_direction = "North"
                elif dy < 0:
                    new_direction = "South"
                else:
                    new_direction = aircraft["direction"]
                aircraft["position"]["x"] = new_x
                aircraft["position"]["y"] = new_y
                aircraft["direction"] = new_direction
                if aircraft_id in self.detected:
                    self.detected.remove(aircraft_id)
                print(f"  Aircraft {aircraft_id} position updated: ({old_x}, {old_y}) to ({new_x}, {new_y}) , New Direction: {new_direction}")
                return True
        return False

    def recognize_aircraft(self, aircraft):
        if aircraft["id"] in self.friendly_ids:
            return "Friendly"
        elif self.airspace.is_inside(aircraft["position"]):
            return "Unknown"
        else:
            return "not friendly"