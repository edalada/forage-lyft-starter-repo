#from datetime import datetime
import sys
sys.path.insert(0,r"C:\Users\HP\internship\forage\engine")
sys.path.insert(0,r"c:\\Users\\HP\\internship\\forage\\engine\\battery")
from battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(WilloughbyEngine,NubbinBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
