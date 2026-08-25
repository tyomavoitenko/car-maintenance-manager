from dataclasses import dataclass
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory

@dataclass
class ServiceRecord:
    date: date
    mileage_km: int
    description: str
    parts_cost: float = 0.0
    labor_cost: float = 0.0
    category: MaintenanceCategory | None = None
    workshop: str | None = None
    notes: str | None = None

    def __str__(self):
        return f"{self.date} — {self.mileage_km:,} km — {self.description} — Parts cost: {self.parts_cost:.2f} PLN, labor cost: {self.labor_cost:.2f} PLN"