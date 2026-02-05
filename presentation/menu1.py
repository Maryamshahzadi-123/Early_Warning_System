from services.aircraft_services import AircraftService


class Menu:
    def __init__(self, aircraft_service=None):
        if aircraft_service is None:
            aircraft_service = AircraftService()
        self.aircraft_service = aircraft_service

    def show(self):
        while True:
            choice = self.show_main_menu()

            if choice == "1":
                self.view_airspace()
            elif choice == "2":
                print("Exiting the system")
                break
            else:
                print("Invalid option")

    def show_main_menu(self):
        print("1. View Nearby Airspace")
        print("2. Exit")
        return input("Select option: ")

    # FR-01
    def view_airspace(self):
        aircrafts = self.aircraft_service.aircrafts

        if not aircrafts:
            print("No aircraft detected")
            input("Press Enter:")
            return
        input("Press Enter:")
