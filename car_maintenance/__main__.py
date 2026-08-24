from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date

vehicle = Vehicle(
    manufacturer="VW",
    model="Golf",
    year=2001,
    engine="1.9 TDI",
    mileage_km=280_000,
)

record_1 = ServiceRecord(
    date=date(2026, 7, 20),
    mileage_km=275_000,
    description="Clutch replacement",
    parts_cost=350.00,
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