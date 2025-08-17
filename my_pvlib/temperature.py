# temperature.py
def estimate_module_temperature(ambient_temp, irradiance):
    """Estimate module temperature based on ambient temperature and irradiance."""
    return ambient_temp + 0.03 * irradiance
