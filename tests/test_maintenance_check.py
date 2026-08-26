from datetime import date
from car_maintenance.maintenance_check import check_maintenance, MaintenanceStatus
from dateutil.relativedelta import relativedelta
import pytest
import tests.helper as helper

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
    vehicle = helper.get_vehicle(vehicle_mileage_km)
    service_record = helper.get_service_record(
        mileage_km=service_mileage_km, 
        service_date=service_date,
    )
    vehicle.add_service_record(service_record)
    maintenance_check = check_maintenance(
        rule=helper.get_rule(), 
        vehicle=vehicle,
    )
    assert maintenance_check.status == status


def test_unknown_status():
    maintenance_check = check_maintenance(
        rule=helper.get_rule(), 
        vehicle=helper.get_vehicle(),
    )
    assert maintenance_check.status == MaintenanceStatus.UNKNOWN