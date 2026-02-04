from services.aircraft_services import AircraftService


class Menu:
    def __init__(self, aircraft_service=None):
        if aircraft_service is None:
            aircraft_service = AircraftService()
        self.aircraft_service = aircraft_service

    def show(self):
        self.show_main_menu()

    def show_main_menu(self):
        print("=== Early Warning System ===")
        print("1. Add Aircraft")
        print("2. Identify Aircraft")
        print("3. Track Aircraft")
        print("4. Exit")
        print("==============================")
        choice = input("Select an option: ")
        return choice