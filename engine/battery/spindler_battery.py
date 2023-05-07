from abc import ABC
from batterys import Battery
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage")
#print(sys.path)
from car import Car
from datetime import datetime
#datetime.today().date()
class SpindlerBattery(Battery,Car, ABC):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date <datetime.today().date():
            return True
        else:
            return False