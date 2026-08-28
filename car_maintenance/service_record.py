from dataclasses import dataclass
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory

@dataclass
class ServiceRecord:
    category: MaintenanceCategory
    date: date
    mileage_km: int

    def __str__(self):
        return f"{self.date} — {self.mileage_km:,} km — {self.category.value}"