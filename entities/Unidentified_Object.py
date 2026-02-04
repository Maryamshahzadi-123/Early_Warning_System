class Airspace:
    def __init__(self):
        self.aircrafts = []
        self.unidentified_objects = []
    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)
    def add_unidentified_object(self, obj):
        self.unidentified_objects.append(obj)


