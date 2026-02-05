class AlertService:
    def __init__(self):
        self.alerts = []

    def generate_alert(self, alert):
        self.alerts.append(alert)
        print(f"ALERT: {alert.alert_type} at position {alert.position}")

    def get_alerts(self):
        return self.alerts

         
        
