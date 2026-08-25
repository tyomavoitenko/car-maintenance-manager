from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_check import check_maintenance
from car_maintenance.maintenance_rule import MaintenanceRule

golf = Vehicle(
    manufacturer="VW",
    model="Golf",
    year=2001,
    engine="1.9 TDI",
    mileage_km=280_500,
)

oil_change = ServiceRecord(
    date=date(2025, 9, 15),
    mileage_km=280_000,
    description="Oil change",
    parts_cost=200.00,
    category=MaintenanceCategory.ENGINE_OIL_AND_FILTER
)
golf.add_service_record(oil_change)

golf_engine_oil_rule = MaintenanceRule(
    category=MaintenanceCategory.ENGINE_OIL_AND_FILTER,
    description="Engine oil and filter maintenance rule for my Golf Mk4",
    interval_km=10_000,
    interval_months=12,
)

maintenance_check = check_maintenance(
    rule=golf_engine_oil_rule, 
    vehicle=golf,
)

print("Status: ", maintenance_check.status.name)
print("Next due(km): ", maintenance_check.next_due_km)
print("Next due date: ", maintenance_check.next_due_date)