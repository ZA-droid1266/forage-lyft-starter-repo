from car import Car
from engines import Engine
from batteries import Battery 

def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    newCar = Car(CapuletEngine(last_service_mileage,current_mileage),SpindlerBattery(last_service_date,current_date))

def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    newCar = Car(WilloughbyEngine(last_service_mileage,current_mileage),SpindlerBattery(last_service_date,current_date))

def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
    newCar = Car(SternmanEngine(last_service_mileage,current_mileage),SpindlerBattery(last_service_date,current_date))

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    newCar = Car(WilloughbyEngine(last_service_mileage,current_mileage),NubbinBattery(last_service_date,current_date))

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    newCar = Car(CapuletEngine(last_service_mileage,current_mileage),NubbinBattery(last_service_date,current_date))
