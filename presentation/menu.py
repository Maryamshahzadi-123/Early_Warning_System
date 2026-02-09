from services.aircraft_services import AircraftService
import threading, time, random
class Menu:
    def __init__(self, aircraft_service=None):
        if aircraft_service is None:
            aircraft_service = AircraftService()
        self.aircraft_service = aircraft_service
        self.aircrafts = []      # Add this
        self.scanning = True     # Add this too
            
  
    def show(self):
     while True:
        choice = self.show_main_menu()
        if choice == "1":
            self.view_airspace()
        elif choice =="2":
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

    
    #FR-02:  continuously scan the airspace using radar
    
    def start_radar(self):
        radar_thread = threading.Thread(
            target=self.scan_airspace,
            daemon=True  # daemon=True: jab main program band ho, yeh thread bhi automatic band ho jaye
        )
        radar_thread.start()

    def scan_airspace(self):
        while self.scanning:
            time.sleep(10)   # radar scans  after every 10 seconds
           
            aircraft = {  # fake aircraft generate
                "id": f"AC-{random.randint(100, 999)}",
                "altitude": random.randint(1000, 40000)
            }

            self.aircrafts.append(aircraft)
            print(f"[RADAR] Aircraft detected: {aircraft['id']}")
    



   