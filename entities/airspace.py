class airspace:
    def __init__(self):
        self.aircrafts = []
    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)
        
        
    #_F3
    def is_inside(self, position):
        return 0 <= position["x"] <= 100 and 0 <= position["y"] <= 100

            

