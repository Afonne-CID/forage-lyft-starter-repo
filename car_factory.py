from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

from typing import List

from car import Car


class CarFactory:

    @staticmethod
    def create_calliope(tire_wear: List[int], current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)

        car = Car()
        car.engine = engine
        car.battery = battery
        car.tire = tire

        return car

    @staticmethod
    def create_glissade(tire_wear: List[int], current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)

        car = Car()
        car.engine = engine
        car.battery = battery
        car.tire = tire

        return car

    @staticmethod
    def create_palindrome(tire_wear: List[int], current_date: datetime, last_service_date: datetime, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tire_wear)

        car = Car()
        car.engine = engine
        car.battery = battery
        car.tire = tire

        return car

    @staticmethod
    def create_rorschach(tire_wear: List[int], current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)

        car = Car()
        car.engine = engine
        car.battery = battery
        car.tire = tire

        return car

    @staticmethod
    def create_thovex(tire_wear: List[int], current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tire_wear)

        car = Car()
        car.engine = engine
        car.battery = battery
        car.tire = tire

        return car
