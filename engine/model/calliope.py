#from datetime import datetime
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage\engine")
sys.path.insert(0,r"c:\\Users\\HP\\internship\\forage\\engine\\battery")
#print(sys.path)
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine,SpindlerBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
