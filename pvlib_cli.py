# pvlib_cli.py


import argparse
import pandas as pd
from src.pvsystem import PVSystem, Location
from src.modelchain import ModelChain


def main():
    parser = argparse.ArgumentParser(description="Run PV simulation with pvlib.")
    parser.add_argument("--lat", type=float, required=True, help="Latitude")
    parser.add_argument("--lon", type=float, required=True, help="Longitude")
    parser.add_argument("--tilt", type=float, default=30.0)
    parser.add_argument("--azimuth", type=float, default=180.0)
    parser.add_argument("--irradiance_csv", type=str, required=True)
    parser.add_argument("--output_csv", type=str, default="ac_output.csv")

    args = parser.parse_args()
    data = pd.read_csv(args.irradiance_csv, index_col=0, parse_dates=True)

    site = Location(args.lat, args.lon)
    system = PVSystem(surface_tilt=args.tilt, surface_azimuth=args.azimuth)
    mc = ModelChain(system, site)
    mc.run_model(data)

    output = mc.ac
    output.to_csv(args.output_csv)
    print("completed")

if __name__ == "__main__":
    main()



