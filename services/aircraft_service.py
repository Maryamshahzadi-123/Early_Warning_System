from data_layer.db_context import DbContext
from entities.aircraft import Aircraft
from typing import Optional


class AircraftService:
    @staticmethod
    def get_aircraft_by_id(aircraft_id: int) -> Optional[Aircraft]:
        for aircraft in DbContext.aircraft:
            if aircraft.id == aircraft_id:
                return aircraft
        return None

    @staticmethod
    def get_aircraft_by_tail_number(tail_number: str) -> Optional[Aircraft]:
        for aircraft in DbContext.aircraft:
            if aircraft.tail_number == tail_number:
                return aircraft
        return None

    def create_aircraft(self, tail_number: str, model: str, manufacturer: str, year: Optional[int] = None) -> Aircraft:
        existing = self.get_aircraft_by_tail_number(tail_number)
        if existing:
            raise ValueError("Aircraft with this tail number already exists")

        new_id = max([a.id for a in DbContext.aircraft], default=0) + 1
        new_aircraft = Aircraft(id=new_id, tail_number=tail_number, model=model, manufacturer=manufacturer, year=year)
        DbContext.aircraft.append(new_aircraft)
        return new_aircraft

    def update_aircraft(self, aircraft_id: int, tail_number: Optional[str] = None, model: Optional[str] = None, manufacturer: Optional[str] = None, year: Optional[int] = None) -> Aircraft:
        aircraft = self.get_aircraft_by_id(aircraft_id)
        if aircraft is None:
            raise ValueError("Aircraft not found")

        if tail_number:
            aircraft.tail_number = tail_number
        if model:
            aircraft.model = model
        if manufacturer:
            aircraft.manufacturer = manufacturer
        if year is not None:
            aircraft.year = year

        return aircraft

    def delete_aircraft(self, aircraft_id: int) -> None:
        aircraft = self.get_aircraft_by_id(aircraft_id)
        if aircraft is None:
            raise ValueError("Aircraft not found")

        DbContext.aircraft.remove(aircraft)

    def get_all_aircraft(self) -> list[Aircraft]:
        return DbContext.aircraft
