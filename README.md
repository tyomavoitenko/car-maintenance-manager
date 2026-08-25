# Car Maintenance Manager

A command-line application for tracking a vehicle's complete maintenance and repair history, and telling you what maintenance is coming up — or already overdue — based on mileage and time intervals.

This is a personal learning project, built from scratch to learn Python properly (beyond basic syntax) by building something real: a typed domain model, automated tests, and a CLI, evolving incrementally milestone by milestone rather than all at once.

## What it does so far

- Track a vehicle's basic details (manufacturer, model, year, engine, mileage).
- Log service and repair records against a vehicle, with dates, mileage, and costs.
- Define recurring maintenance rules (e.g. "engine oil every 10,000 km or 12 months") and automatically calculate whether each one is OK, due soon, overdue, or has no service history yet.

This is a work in progress — persistence, interactive input, and a full maintenance dashboard are still to come.

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

Run the tests:

```bash
python -m pytest -v
```

## License

Copyright © 2026 Artem Voitenko. All rights reserved.

This project is provided for portfolio and educational viewing purposes only. No permission is granted to copy, modify, distribute, or use the source code without prior written permission.

The software is provided "as is", without warranty of any kind. The author is not liable for any damages or losses arising from its use.
