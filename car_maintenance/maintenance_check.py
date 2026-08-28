from dataclasses import dataclass
from datetime import date
from enum import Enum

from dateutil.relativedelta import relativedelta

from car_maintenance.maintenance_rule import MaintenanceRule
from car_maintenance.vehicle import Vehicle

DUE_SOON_KM = 1000
DUE_SOON_MONTHS = 1

class MaintenanceStatus(Enum):
    OK = "OK"
    DUE_SOON = "DUE SOON"
    OVERDUE = "OVERDUE"
    UNKNOWN = "UNKNOWN"

@dataclass
class MaintenanceCheck:
    rule: MaintenanceRule
    status: MaintenanceStatus
    last_service_date: date | None = None
    last_service_mileage: int | None = None
    next_due_date: date | None = None
    next_due_km: int | None = None

def check_maintenance(rule: MaintenanceRule, vehicle: Vehicle) -> MaintenanceCheck:
    last_service = max(
        (r for r in vehicle.service_records if r.category == rule.category), 
        key=lambda r: r.date, 
        default=None
    )

    if last_service is None:
        return MaintenanceCheck(
            rule=rule,
            status=MaintenanceStatus.UNKNOWN
        )

    next_due_km = None
    if rule.interval_km is not None:
        next_due_km = last_service.mileage_km + rule.interval_km

    next_due_date = None
    if rule.interval_months is not None:
        next_due_date = last_service.date + relativedelta(months=rule.interval_months)

    if is_overdue_km(vehicle.mileage_km, next_due_km) or is_overdue_date(next_due_date):
        status = MaintenanceStatus.OVERDUE
    elif is_overdue_km(vehicle.mileage_km + DUE_SOON_KM, next_due_km) or is_due_soon_date(next_due_date):
        status = MaintenanceStatus.DUE_SOON
    else:
        status = MaintenanceStatus.OK

    return MaintenanceCheck(
        rule=rule,
        status=status,
        last_service_date=last_service.date,
        last_service_mileage=last_service.mileage_km,
        next_due_date=next_due_date,
        next_due_km=next_due_km,
    )


def is_overdue_km(current_km: int, next_due_km: int | None) -> bool:
    return next_due_km is not None and current_km >= next_due_km


def is_overdue_date(next_due_date: date | None) -> bool:
    return next_due_date is not None and date.today() >= next_due_date


def is_due_soon_date(next_due_date: date | None) -> bool:
    return next_due_date is not None and date.today() + relativedelta(months=DUE_SOON_MONTHS) >= next_due_date