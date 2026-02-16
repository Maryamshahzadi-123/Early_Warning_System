class aircraft:
    def __init__(self, aircraft_id, aircraft_type, position ,quadrant):
        self.aircraft_id = aircraft_id
        self.aircraft_type = aircraft_type
        self.position = position 
        self.quadrant = quadrant  
        
    def update_position(self,new_position):
        self.position =new_position
            