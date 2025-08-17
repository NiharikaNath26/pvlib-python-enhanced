# test_cli.py
import subprocess
import os

def test_cli_runs():
    # Assume sample irradiance file is present
    sample_csv = "sample_irradiance.csv"
    with open(sample_csv, "w") as f:
        f.write("timestamp,ghi,dni,dhi
2023-01-01 12:00:00,800,600,200
")

    cmd = [
        "python", "pvlib_cli.py",
        "--lat", "35",
        "--lon", "-110",
        "--irradiance_csv", sample_csv,
        "--output_csv", "out.csv"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert "completed" in result.stdout.lower()
    os.remove("out.csv")
    os.remove(sample_csv)
