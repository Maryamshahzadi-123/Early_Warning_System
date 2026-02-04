class UnknownObjectService:
    def __init__(self):
        self.unknown_objects = []
        self.alerts = []
    def detect_object(self, obj):
        self.unknown_objects.append(obj)
        alert = {
            "object_id": getattr(obj, "object_id", "Unknown"),
            "alert_type": "Unknown Object Detected",
            "position": getattr(obj, "position", None)
        }
        self.alerts.append(alert)
        return alert
    def track_object(self, obj):
        return getattr(obj, "position", None), getattr(obj, "movement", None)