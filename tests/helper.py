from datetime import date

from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_rule import MaintenanceRule
from car_maintenance.service_record import ServiceRecord
from car_maintenance.vehicle import Vehicle


def get_vehicle(mileage_km: int = 300_000):
    return Vehicle(
        manufacturer="VW",
        model="Golf",
        year=2001,
        engine="1.9 TDI",
        mileage_km=mileage_km,
    )


def get_rule():
    return MaintenanceRule(
        category=MaintenanceCategory.ENGINE_OIL_AND_FILTER,
        interval_km=10_000,
        interval_months=12,
    )


def get_service_record(mileage_km: int, service_date: date):
    return ServiceRecord(
        category=MaintenanceCategory.ENGINE_OIL_AND_FILTER,
        mileage_km=mileage_km,
        date=service_date,
    )