from dataclasses import dataclass

from car_maintenance.maintenance_category import MaintenanceCategory


class InvalidMaintenanceRuleError(Exception):
    pass

@dataclass
class MaintenanceRule:
    category: MaintenanceCategory
    interval_km: int | None = None
    interval_months: int | None = None

    def __post_init__(self):
        if self.interval_km is None and self.interval_months is None:
            raise InvalidMaintenanceRuleError("Either interval_km or interval_months field should be set.")
        if self.interval_km is not None and self.interval_km <= 0:
            raise InvalidMaintenanceRuleError("interval_km must be greater than zero")
        if self.interval_months is not None and self.interval_months <= 0:
            raise InvalidMaintenanceRuleError("interval_months must be greater than zero")



