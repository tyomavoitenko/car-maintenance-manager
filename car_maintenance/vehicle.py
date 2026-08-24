from dataclasses import dataclass, field
from car_maintenance.service_record import ServiceRecord


@dataclass
class Vehicle:
    manufacturer: str
    model: str
    year: int
    engine: str
    mileage_km: int
    vin: str | None = None
    registration_number: str | None = None
    notes: str | None = None
    service_records: list[ServiceRecord] = field(default_factory=list)

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}, {self.engine} — {self.mileage_km:,} km"

    def add_service_record(self, record: ServiceRecord) -> None:
        self.service_records.append(record)