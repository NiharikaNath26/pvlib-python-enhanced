# pvsystem.py

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class PVSystem:
    def __init__(self, surface_tilt, surface_azimuth):
        self.surface_tilt = surface_tilt
        self.surface_azimuth = surface_azimuth

from src.module import calculate_module_efficiency
from src.inverter import calculate_inverter_output
from src.temperature import estimate_module_temperature

__all__ = [
    "Location",
    "PVSystem",
    "calculate_module_efficiency",
    "calculate_inverter_output",
    "estimate_module_temperature"
]




