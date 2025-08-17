# my_pvlib/modelchain.py

class ModelChain:
    def __init__(self, system, location):
        self.system = system
        self.location = location
        self.ac = None

    def run_model(self, data):
        self.ac = data["ghi"] * 0.001  # dummy output, just for testing
