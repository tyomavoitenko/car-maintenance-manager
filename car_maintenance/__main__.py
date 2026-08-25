from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory

vehicle = Vehicle(
    manufacturer="VW",
    model="Golf",
    year=2001,
    engine="1.9 TDI",
    mileage_km=280_000,
)

record_1 = ServiceRecord(
    date=date(2026, 3, 15),
    mileage_km=280_000,
    description="Oil change",
    parts_cost=200.00,
    category=MaintenanceCategory.ENGINE_OIL_AND_FILTER
)

record_2 = ServiceRecord(
    date=date(2026, 8, 12),
    mileage_km=277_256,
    description="Front coil springs replacement",
    parts_cost=115.00,
)

vehicle.add_service_record(record_1)
vehicle.add_service_record(record_2)

print(vehicle)

for record in sorted(vehicle.service_records, key=lambda r: r.date):
    print(record)