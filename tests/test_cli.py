# test_cli.py
import sys
import os
import subprocess

# Add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_cli_runs():
    # Create a sample irradiance CSV file
    sample_csv = "sample_irradiance.csv"
    with open(sample_csv, "w") as f:
        f.write("timestamp,ghi,dni,dhi\n")
        f.write("2023-01-01 12:00:00,800,600,200\n")

    cmd = [
        "python", "pvlib_cli.py",
        "--lat", "35",
        "--lon", "-110",
        "--irradiance_csv", sample_csv,
        "--output_csv", "out.csv"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)

    assert "completed" in result.stdout.lower()

    os.remove("out.csv")
    os.remove(sample_csv)


