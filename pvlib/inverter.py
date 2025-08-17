# inverter.py
def calculate_inverter_output(dc_power, efficiency=0.96):
    """Convert DC power to AC using inverter efficiency."""
    return dc_power * efficiency
