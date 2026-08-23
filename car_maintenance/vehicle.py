from dataclasses import dataclass

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