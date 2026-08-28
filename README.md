# Car Maintenance Manager

A command-line application for tracking a vehicle's complete maintenance and repair history, and telling you what maintenance is coming up — or already overdue — based on mileage and time intervals.

This is a personal learning project, built from scratch to learn Python properly (beyond basic syntax) by building something real: a typed domain model, automated tests, and a CLI, evolving incrementally milestone by milestone rather than all at once.

## What it does so far

This project is deliberately scoped to **recurring maintenance tracking only** — not general repair history, costs, or notes. It answers one question: for a given vehicle, what maintenance is due, and when.

- Track a vehicle's basic details (manufacturer, model, year, engine, current mileage).
- Log maintenance events by category (e.g. engine oil, brake fluid, spark plugs) and mileage/date.
- Define recurring maintenance rules (e.g. "engine oil every 10,000 km or 12 months").
- Maintenance dashboard — checks every rule against the vehicle's real history and current mileage, reporting OK, due soon, overdue, or no history recorded, with km/days remaining.
- Save and load a vehicle's data to/from a local JSON file, so it survives between runs.
- Interactive CLI menu for all of the above — no code editing required to use the app.

**Coming up:** a repository polish pass with CI, support for tracking more than one vehicle, and support for miles as an alternative to kilometers (currently hardcoded).

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

The first run prompts you to enter your vehicle's details; subsequent runs load `data/vehicle.json` and drop you straight into the menu. This file is gitignored — it's local runtime state, not source code.

Run the tests:

```bash
python -m pytest -v
```

## License

Copyright © 2026 Artem Voitenko.

This project is shared for portfolio and educational purposes.

The software is provided "as is", without warranty of any kind. The author is not liable for any damages or losses arising from its use.
