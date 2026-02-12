from services.aircraft_services import AircraftService
import time
import random

class Menu:
    def __init__(self, aircraft_service=None):
        if aircraft_service is None:
            aircraft_service = AircraftService()
        self.aircraft_service = aircraft_service
        self.aircraft = []
        self.scanning = True
        
    #2
    def scan_airspace(self):
        aircraft = {
            "id": f"AC-{random.randint(100, 999)}",
            "altitude": random.randint(1000, 40000)
        }
        self.aircraft.append(aircraft)
        print(f"[RADAR] Aircraft detected: {aircraft['id']}")

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
        print("1 : view nearby airspace")
        print("2 : Exit")
        return input("select option :")

    #FR-01 see the nearby airspace
    def view_airspace(self):
        aircrafts = self.aircraft_service.aircrafts

        if not aircrafts:
            print("No aircraft detected")
            input("Press Enter:")
            return
        input("Press Enter:")
        for aircraft in aircrafts:
            print(aircraft)

    #2
    def view_scanned_airspace(self):
        self.scan_airspace()   

        aircraft = self.aircraft
        if not aircraft:
            print("No aircraft detected")
            input("Press Enter:")
            return

        for a in aircraft:
            print(a)
