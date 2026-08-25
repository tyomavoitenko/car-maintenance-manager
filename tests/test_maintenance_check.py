from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_check import check_maintenance, MaintenanceStatus
from car_maintenance.maintenance_rule import MaintenanceRule
from dateutil.relativedelta import relativedelta
import pytest

@pytest.mark.parametrize("vehicle_mileage_km, service_mileage_km, service_date, status", [
    pytest.param(
        100_000, 
        85_000, 
        date.today() - relativedelta(months=6), 
        MaintenanceStatus.OVERDUE,
        id="overdue_by_mileage",
    ),
    pytest.param(
        100_000, 
        95_000, 
        date.today() - relativedelta(months=24), 
        MaintenanceStatus.OVERDUE,
        id="overdue_by_date",
    ),
    pytest.param(
        100_000, 
        90_500, 
        date.today() - relativedelta(months=6), 
        MaintenanceStatus.DUE_SOON,
        id="due_soon_by_mileage",
    ),
    pytest.param(
        100_000, 
        95_000, 
        date.today() - relativedelta(days=350), 
        MaintenanceStatus.DUE_SOON,
        id="due_soon_by_date",
    ),
    pytest.param(
        100_000, 
        95_000, 
        date.today() - relativedelta(months=6), 
        MaintenanceStatus.OK,
        id="ok",
    ),
])
def test_overdue_due_soon_ok_statuses(vehicle_mileage_km, service_mileage_km, service_date, status):
    vehicle = get_vehicle(vehicle_mileage_km)
    service_record = get_service_record(
        mileage_km=service_mileage_km, 
        service_date=service_date,
    )
    vehicle.add_service_record(service_record)
    maintenance_check = check_maintenance(
        rule=get_rule(), 
        vehicle=vehicle,
    )
    assert maintenance_check.status == status


def test_unknown_status():
    maintenance_check = check_maintenance(
        rule=get_rule(), 
        vehicle=get_vehicle(),
    )
    assert maintenance_check.status == MaintenanceStatus.UNKNOWN


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
        description="Engine oil and filter maintenance rule",
        interval_km=10_000,
        interval_months=12,
    )


def get_service_record(mileage_km: int, service_date: date):
    return ServiceRecord(
        date=service_date,
        mileage_km=mileage_km,
        description="Oil change",
        category=MaintenanceCategory.ENGINE_OIL_AND_FILTER
    )

