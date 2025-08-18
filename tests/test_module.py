import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.module import calculate_module_efficiency

def test_efficiency():
    assert calculate_module_efficiency({"efficiency": 0.2}) == 0.2


