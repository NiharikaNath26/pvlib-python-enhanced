
# pvlib-python Enhanced Implementation

This repository is a fork-style enhancement of the `pvlib-python` library, submitted as part of the Turing onboarding assessment.

## 📌 Overview

This enhanced version includes the implementation of three production-grade prompts:

### ✅ Prompt 1: Modularize `pvsystem.py`
- Extracted functionality into:
  - `module.py` — handles PV module logic
  - `inverter.py` — models inverter output
  - `temperature.py` — estimates temperature from irradiance
- Improves maintainability and structure

### ✅ Prompt 2: Add CLI for PV Simulation
- `pvlib_cli.py`: Run a full PV simulation via command line
- Input: latitude, longitude, tilt, azimuth, irradiance CSV
- Output: AC power results

### ✅ Prompt 3: Add Multiprocessing for Batch ModelChain Simulations
- `batch_runner.py`: Parallelizes multiple PV simulations using `multiprocessing.Pool`
- Optimized for high-throughput environments

---

## 🧪 Running Tests

```bash
pip install -r requirements.txt
pytest tests/
```

---

## 🚀 Run the CLI Tool

```bash
python pvlib_cli.py --lat 35 --lon -110 --irradiance_csv input.csv --output_csv output.csv
```

---

## ⚡ Run Batch Simulations

```python
from pvlib.batch_runner import run_batch_simulations
```

Prepare a list of configs as `(lat, lon, tilt, azimuth, irradiance_df)` and pass it to the function.

---

## 🛠 Requirements

- Python 3.8+
- pvlib
- pandas
- numpy
- pytest (for tests)

---

## 📁 Structure

```
pvlib/
├── module.py
├── inverter.py
├── temperature.py
├── pvsystem.py
├── batch_runner.py

pvlib_cli.py
tests/
```

---

## License

This project is a candidate enhancement submitted for educational and review purposes. All original code © pvlib contributors.
