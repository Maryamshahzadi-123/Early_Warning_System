class TrackingService:
    def __init__(self):
        self.tracked_objects = {}
    def start_tracking(self, obj_id, position, movement):
        self.tracked_objects[obj_id] = {"position": position, "movement": movement}
    def update_tracking(self, obj_id, position, movement):
        if obj_id in self.tracked_objects:
            self.tracked_objects[obj_id]["position"] = position
            self.tracked_objects[obj_id]["movement"] = movement
    def stop_tracking(self, obj_id):
        if obj_id in self.tracked_objects:
            del self.tracked_objects[obj_id]
    def get_tracked_info(self, obj_id):
        return self.tracked_objects.get(obj_id, None)
    
