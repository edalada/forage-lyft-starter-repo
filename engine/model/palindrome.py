#from datetime import datetime
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage\engine")
sys.path.insert(0,r"C:\Users\HP\internship\forage")
sys.path.insert(0,r"c:\\Users\\HP\\internship\\forage\\engine\\battery")
from battery.nubbin_battery import NubbinBattery
from car import Car
from engine.sternman_engine import SternmanEngine


class Palindrome(SternmanEngine,NubbinBattery):
    def __init__(self, last_service_date,warning_light_is_on):
        super().__init__(last_service_date)
        self.last_service_date=last_service_date
        self.warning_light_is_on=warning_light_is_on
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False

