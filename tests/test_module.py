# test_module.py
from pvlib.module import calculate_module_efficiency

def test_efficiency():
    assert calculate_module_efficiency({"efficiency": 0.2}) == 0.2
