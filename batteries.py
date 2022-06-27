import time
from car import Car

class Battery():

    def needs_service():
        return False

class SpindlerBattery(Batteries):
    def __init__(self, nlast_service_date, ncurrent_date):
        self.last_service_date = nlast_service_date
        self.current_date = ncurrent_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < self.current_date
            
class NubbinBattery(Batteries):
    def __init__(self, nlast_service_date, ncurrent_date):
        self.last_service_date = nlast_service_date
        self.current_date = ncurrent_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < self.current_date
        
