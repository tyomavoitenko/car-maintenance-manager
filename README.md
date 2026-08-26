# Car Maintenance Manager

A command-line application for tracking a vehicle's complete maintenance and repair history, and telling you what maintenance is coming up — or already overdue — based on mileage and time intervals.

This is a personal learning project, built from scratch to learn Python properly (beyond basic syntax) by building something real: a typed domain model, automated tests, and a CLI, evolving incrementally milestone by milestone rather than all at once.

## What it does so far

- Track a vehicle's basic details (manufacturer, model, year, engine, mileage).
- Log service and repair records against a vehicle, with dates, mileage, and costs.
- Define recurring maintenance rules (e.g. "engine oil every 10,000 km or 12 months") and automatically calculate whether each one is OK, due soon, overdue, or has no service history yet.
- Save and load a vehicle's data to/from a local JSON file, so it survives between runs.
- Interactive CLI menu — add service records and view service history without editing code.

This is a work in progress — a full maintenance dashboard covering multiple rules, and support for more than one vehicle, are still to come.

## Tech stack

- Python 3.14
- [`python-dateutil`](https://pypi.org/project/python-dateutil/) for calendar-correct date arithmetic
- [`pytest`](https://pytest.org/) for testing

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

Run the app:

```bash
python -m car_maintenance
```

The first run creates `data/vehicle.json` with sample data; subsequent runs load and reuse it. This file is gitignored — it's local runtime state, not source code.

Run the tests:

```bash
python -m pytest -v
```

## License

Copyright © 2026 Artem Voitenko.

This project is shared for portfolio and educational purposes.

The software is provided "as is", without warranty of any kind. The author is not liable for any damages or losses arising from its use.
