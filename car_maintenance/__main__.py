from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_check import check_maintenance
from car_maintenance.maintenance_rule import MaintenanceRule
import car_maintenance.storage as storage

try:
    vehicle = storage.load_vehicle("data/vehicle.json")
except FileNotFoundError:
    vehicle = Vehicle(
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
    air_filter_change = ServiceRecord(
        date=date(2025, 12, 4),
        mileage_km=283_000,
        description="Air filter change",
        parts_cost=25.00,
        category=MaintenanceCategory.AIR_FILTER
    )
    vehicle.add_service_record(oil_change)
    vehicle.add_service_record(air_filter_change)

    storage.save_vehicle(vehicle, path="data/vehicle.json")


engine_oil_rule = MaintenanceRule(
    category=MaintenanceCategory.ENGINE_OIL_AND_FILTER,
    description="Engine oil and filter maintenance rule for my Golf Mk4",
    interval_km=10_000,
    interval_months=12,
)
maintenance_check = check_maintenance(
    rule=engine_oil_rule, 
    vehicle=vehicle,
)
print(vehicle)
print(maintenance_check)