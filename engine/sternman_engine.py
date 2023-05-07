from abc import ABC
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage")
from engines import Engine
from car import Car


class SternmanEngine(Engine,Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
