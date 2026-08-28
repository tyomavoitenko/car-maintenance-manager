from dataclasses import dataclass, field
from car_maintenance.service_record import ServiceRecord
from car_maintenance.maintenance_rule import MaintenanceRule

@dataclass
class Vehicle:
    manufacturer: str
    model: str
    year: int
    engine: str
    mileage_km: int
    service_records: list[ServiceRecord] = field(default_factory=list[ServiceRecord])
    maintenance_rules: list[MaintenanceRule] = field(default_factory=list[MaintenanceRule])

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}, {self.engine} — {self.mileage_km:,} km"

    def add_service_record(self, record: ServiceRecord) -> None:
        self.service_records.append(record)

    def add_maintenance_rule(self, rule: MaintenanceRule) -> None:
        self.maintenance_rules.append(rule)

    def update_mileage(self, new_mileage_km: int) -> None:
        self.mileage_km = new_mileage_km