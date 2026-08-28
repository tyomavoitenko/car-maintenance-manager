import json
from datetime import date
from enum import Enum
from car_maintenance.vehicle import Vehicle
import dataclasses
from car_maintenance.service_record import ServiceRecord
from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_rule import MaintenanceRule
from pathlib import Path

def _json_default(obj: object) -> object:
    if isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, Enum):
        return obj.value
    else: 
        raise TypeError(f"Cannot serialize {type(obj)}")


def save_vehicle(vehicle: Vehicle, path: str | Path) -> None:
    with open(path, "w") as file:
        json.dump(
            dataclasses.asdict(vehicle),
            file,
            default=_json_default,
            indent=2,
        )


def load_vehicle(path: str | Path) -> Vehicle:
    with open(path) as file:
        data = json.load(file)

        service_records: list[ServiceRecord] = []
        for r in data["service_records"]:
            service_records.append(ServiceRecord(
                category=MaintenanceCategory(r["category"]),
                mileage_km=r["mileage_km"],
                date=date.fromisoformat(r["date"]),
            ))

        maintenance_rules: list[MaintenanceRule] = []
        for r in data.get("maintenance_rules", []):
            maintenance_rules.append(MaintenanceRule(
                category=MaintenanceCategory(r["category"]),
                interval_km=r["interval_km"],
                interval_months=r["interval_months"],
            ))

        return Vehicle(
            manufacturer=data["manufacturer"],
            model=data["model"],
            year=data["year"],
            engine=data["engine"],
            mileage_km=data["mileage_km"],
            service_records=service_records,
            maintenance_rules=maintenance_rules,
        )