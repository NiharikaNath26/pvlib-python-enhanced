# batch_runner.py
import pandas as pd
from multiprocessing import Pool, cpu_count
from pvlib import location, pvsystem, modelchain

def simulate_one_system(config):
    lat, lon, tilt, azimuth, irradiance = config
    site = location.Location(lat, lon)
    system = pvsystem.PVSystem(surface_tilt=tilt, surface_azimuth=azimuth)
    mc = modelchain.ModelChain(system, site)
    mc.run_model(irradiance)
    return mc.ac

def run_batch_simulations(configs, processes=None):
    with Pool(processes or cpu_count()) as pool:
        results = pool.map(simulate_one_system, configs)
    return results
