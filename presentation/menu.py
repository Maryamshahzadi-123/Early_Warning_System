from services.aircraft_services import AircraftService
import time
import random


class Menu:
    def __init__(self, aircraft_service=None, simulation=None):
        if aircraft_service is None:
            aircraft_service = AircraftService()
        self.aircraft_service = aircraft_service
        self.simulation = simulation
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
                self.update_aircraft_position()
            elif choice == "3":
                print("Exiting the system")
                break
            else:
                print("Invalid option")


    def show_main_menu(self):
        print("1 : View nearby airspace")
        print("2 : Update aircraft position")
        print("3 : Exit")
        return input("select option :")

    #F1
    def view_airspace(self):
        if self.simulation:
           self.aircraft_service.detected = []
           self.simulation.run()
        input("Press Enter:")
  

    def update_aircraft_position(self):
        if not self.simulation:
            print(" no simulation data available")
            input("press enter")
            return
        print("  Available IDs: AC001, AC002, AC003, AC004, AC005, AC006, AC007, AC008, AC009, AC010")
        aircraft_id = input("enter aircraft id: ").strip().upper()
        try:
            new_x = int(input("enter new x position: "))
            new_y = int(input("enter new y position: "))
        except ValueError:
            print(" Invalid position")  
            input("press enter:")
            return
        found = self.aircraft_service .update_position(self.simulation.aircraft_data, aircraft_id ,new_x, new_y)
        if not found:
            print(" Aircraft not found")
        input("press enter")
            
                
             
  

    #F2
    def view_scanned_airspace(self):
        self.scan_airspace()   
        aircraft = self.aircraft
        if not aircraft:
            print("No aircraft detected")
            input("Press Enter:")
            return
      

