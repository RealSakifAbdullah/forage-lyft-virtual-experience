from datetime import datetime
from car.car_base import Car

from battery.models.nubbin_battery import NubbinBattery
from battery.models.spindler_battery import SpindlerBattery

from engine.models.capulet_engine import CapuletEngine
from engine.models.sternman_engine import SternmanEngine
from engine.models.willoughby_engine import WilloughbyEngine

from tires.models.carrigan_tires import CarriganTires
from tires.models.octoprime_tires import OctoprimeTires


class CarFactory:

    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)        
        return car

    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_wear):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car
