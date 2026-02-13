from services.data_simulation import DataSimulation
from services.aircraft_services import AircraftService
from presentation.menu import Menu # F3

if __name__ == "__main__":   #F3
     aircraft_service = AircraftService()
     simulation = DataSimulation(aircraft_service)
     menu = Menu(aircraft_service, simulation)
     menu.show()



