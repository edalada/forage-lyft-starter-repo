from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tyre.carigan_tyre import CariganTyre
from tyre.octoprime_tyre import OctoprimeTyre
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tyre_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tyre=CariganTyre(tyre_array)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tyre_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tyre=CariganTyre(tyre_array)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on,tyre_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tyre=CariganTyre(tyre_array)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tyre_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tyre=OctoprimeTyre(tyre_array)
        car = Car(engine, battery,tyre)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tyre_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tyre=OctoprimeTyre(tyre_array)
        car = Car(engine, battery,tyre)
        return car