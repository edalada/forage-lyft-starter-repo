#from abc import ABC
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage")
from batterys import Battery
from car import Car
from datetime import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        #super().__init__(last_service_date)
        #self.current_service_date = current_service_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date <datetime.today().date():
            return True
        else:
            return False