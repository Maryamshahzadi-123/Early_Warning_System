class Aircraft:
    def __init__(self, id, x, y, aircraft_type, speed, direction):
        self.id = id
        self.position = {"x": x, "y": y}
        self.type = aircraft_type
        self.speed = speed
        self.direction = direction

    def to_dict(self):
        return {
            "id": self.id,
            "position": self.position,
            "type": self.type,
            "speed": self.speed,
            "direction": self.direction
        }

    def update_position(self, x, y):
        old_x = self.position["x"]
        old_y = self.position["y"]
        dx = x - old_x
        dy = y - old_y

        if dx > 0 and dy > 0:
            self.direction = "North-East"
        elif dx < 0 and dy > 0:
            self.direction = "North-West"
        elif dx > 0 and dy < 0:
            self.direction = "South-East"
        elif dx < 0 and dy < 0:
            self.direction = "South-West"
        elif dx > 0:
            self.direction = "East"
        elif dx < 0:
            self.direction = "West"
        elif dy > 0:
            self.direction = "North"
        elif dy < 0:
            self.direction = "South"

        self.position["x"] = x
        self.position["y"] = y

        return {
            "old_position": {"x": old_x, "y": old_y},
            "new_position": {"x": x, "y": y},
            "direction": self.direction
        }
