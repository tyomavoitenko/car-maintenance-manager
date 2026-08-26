import json
from datetime import date
from enum import Enum
from car_maintenance.vehicle import Vehicle
import dataclasses
from car_maintenance.service_record import ServiceRecord
from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_rule import MaintenanceRule
from pathlib import Path

def _json_default(obj):
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

        service_records = []
        for r in data["service_records"]:
            service_records.append(ServiceRecord(
                date=date.fromisoformat(r["date"]),
                mileage_km=r["mileage_km"],
                description=r["description"],
                parts_cost=r["parts_cost"],
                labor_cost=r["labor_cost"],
                category=MaintenanceCategory(r["category"]) if r["category"] is not None else None,
                workshop=r["workshop"],
                notes=r["notes"],
            ))

        maintenance_rules = []
        for r in data.get("maintenance_rules", []):
            maintenance_rules.append(MaintenanceRule(
                category=MaintenanceCategory(r["category"]),
                description=r["description"],
                interval_km=r["interval_km"],
                interval_months=r["interval_months"],
            ))

        return Vehicle(
            manufacturer=data["manufacturer"],
            model=data["model"],
            year=data["year"],
            engine=data["engine"],
            mileage_km=data["mileage_km"],
            vin=data["vin"],
            registration_number=data["registration_number"],
            notes=data["notes"],
            service_records=service_records,
            maintenance_rules=maintenance_rules,
        )