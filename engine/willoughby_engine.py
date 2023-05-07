from abc import ABC
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage")
from engines import Engine
from car import Car


class WilloughbyEngine(Engine,Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
