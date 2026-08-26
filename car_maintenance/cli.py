from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date

def prompt_int(message: str) -> int:
    while True:
        raw = input(message)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid whole number.")


def prompt_float(message: str) -> float:
    while True:
        raw = input(message)
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid decimal number.")


def prompt_date(message: str) -> date:
    while True:
        raw = input(message)
        try:
            return date.fromisoformat(raw)
        except ValueError:
            print("Please enter a valid date in the format yyyy-mm-dd")


def create_vehicle_interactively() -> Vehicle:
    manufacturer = input("Enter manufacturer: ")
    model = input("Enter model: ")
    year = prompt_int("Enter year: ")
    engine = input("Enter engine: ")
    mileage_km = prompt_int("Enter mileage: ")
    vin = input("Enter VIN (optional): ") or None
    registration_number = input("Enter registration number (optional): ") or None
    notes = input("Enter notes (optional): ") or None

    return Vehicle(
        manufacturer=manufacturer,
        model=model,
        year=year,
        engine=engine,
        mileage_km=mileage_km,
        vin=vin,
        registration_number=registration_number,
        notes=notes,
    )


def create_service_record_interactively() -> ServiceRecord:
    service_date = prompt_date("Enter date (yyyy-mm-dd): ")
    mileage_km = prompt_int("Enter mileage (km): ")
    description = input("Enter description: ")
    parts_cost = prompt_float("Enter parts cost: ")
    labor_cost = prompt_float("Enter labor cost: ")
    workshop = input("Enter workshop (optional): ") or None
    notes = input("Enter notes (optional): ") or None

    return ServiceRecord(
        date=service_date,
        mileage_km=mileage_km,
        description=description,
        parts_cost=parts_cost,
        labor_cost=labor_cost,
        workshop=workshop,
        notes=notes,
    )
    
    
def run_menu(vehicle: Vehicle) -> None:
    while True:
        print("1) Add a service record")
        print("2) View service history")
        print("3) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            record = create_service_record_interactively()
            vehicle.add_service_record(record)
        elif choice == "2":
            for record in sorted(vehicle.service_records, key=lambda r: r.date):
                print(record)
        elif choice == "3":
            break
        else:
            print("Not a valid option, try again.")