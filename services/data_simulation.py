# from entities.aircraft import Aircraft
# from services.aircraft_services import AircraftService


# class DataSimulation:
#     def __init__(self, aircraft_service=None):
#         if aircraft_service is None:
#             aircraft_service = AircraftService()
#         self.aircraft_service = aircraft_service

#         # dummy data (10 aircraft)
#         self.aircraft_data = [
#             Aircraft("AC001", 10, 20, "commercial", 300, "North"),
#             Aircraft("AC002", 120, 80, "military", 250, "East"),
#             Aircraft("AC003", 50, 60, "commercial", 190, "south"),
#             Aircraft("AC004", -10, 40, "military", 200, "west"),
#             Aircraft("AC005", 90, 110, "commercial", 280, "North"),
#             Aircraft("AC006", 30, 25, "military", 140, "North"),
#             Aircraft("AC007", 200, 150, "commercial", 240, "East"),
#             Aircraft("AC008", 70, 40, "commercial", 290, "North"),
#             Aircraft("AC009", 15, 95, "military", 310, "west"),
#             Aircraft("AC010", 0, 0, "military", 360, "west"),
#         ]

#     def run(self):
#         for aircraft in self.aircraft_data:
#             self.aircraft_service.process_aircraft(aircraft.to_dict())

#     def get_all_aircraft(self):
#         return self.aircraft_data

#     def get_aircraft_by_id(self, aircraft_id):
#         for aircraft in self.aircraft_data:
#             if aircraft.id == aircraft_id:
#                 return aircraft
#         return None
