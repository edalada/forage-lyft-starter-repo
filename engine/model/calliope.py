#from datetime import datetime
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage\engine")
sys.path.insert(0,r"C:\Users\HP\internship\forage")
sys.path.insert(0,r"c:\\Users\\HP\\internship\\forage\\engine\\battery")
#print(sys.path)
from car import Car
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine,SpindlerBattery,Car):
    def __init__(self, last_service_date,current_mileage, last_service_mileage):
        super().__init__(last_service_date,last_service_mileage)
        self.last_service_date=last_service_date
        self.current_mileage=current_mileage
        self.last_service_mileage=last_service_mileage
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
