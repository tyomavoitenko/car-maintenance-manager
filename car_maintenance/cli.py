from car_maintenance.vehicle import Vehicle
from car_maintenance.service_record import ServiceRecord
from datetime import date
from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_rule import MaintenanceRule, InvalidMaintenanceRuleError
from car_maintenance.maintenance_check import MaintenanceCheck, MaintenanceStatus, check_maintenance

def prompt_int(message: str) -> int:
    while True:
        raw = input(message)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid whole number.")


def prompt_optional_int(message: str) -> int | None:
    while True:
        raw = input(message)
        if not raw.strip():
            return None
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


def prompt_category() -> MaintenanceCategory:
    categories = list(MaintenanceCategory)
    while True:
        for i, c in enumerate(categories, start=1):
            print(f"{i}) {c.value}")
        choice = input("Choose an option: ")
        try:
            return categories[int(choice) - 1]
        except (ValueError, IndexError):
            print("Not a valid option, try again.")


def prompt_optional_category() -> MaintenanceCategory | None:
    categories = list(MaintenanceCategory)
    while True:
        for i, c in enumerate(categories, start=1):
            print(f"{i}) {c.value}")
        choice = input("Choose an option: ")
        if not choice:
            return None
        try:
            return categories[int(choice) - 1]
        except (ValueError, IndexError):
            print("Not a valid option, try again.")


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
    category = prompt_optional_category()
    workshop = input("Enter workshop (optional): ") or None
    notes = input("Enter notes (optional): ") or None

    return ServiceRecord(
        date=service_date,
        mileage_km=mileage_km,
        description=description,
        parts_cost=parts_cost,
        labor_cost=labor_cost,
        category=category,
        workshop=workshop,
        notes=notes,
    )


def create_maintenance_rule_interactively() -> MaintenanceRule:
    while True:
        try:
            category = prompt_category()
            description = input("Enter description: ")
            interval_km = prompt_optional_int("Enter interval (km): ")
            interval_month = prompt_optional_int("Enter interval (months): ")

            return MaintenanceRule(
                category=category,
                description=description,
                interval_km=interval_km,
                interval_months=interval_month,
            )
        except InvalidMaintenanceRuleError:
            print("Invalid rule (make sure you specify an interval). Try again.")


def format_maintenance_check(check: MaintenanceCheck, current_mileage_km: int):
    match check.status:
        case MaintenanceStatus.OK | MaintenanceStatus.DUE_SOON:
            return f"{check.status.value}: {check.rule.description} — {get_remaining(check, current_mileage_km)}"
        case MaintenanceStatus.OVERDUE:
            return f"{check.status.value}: {check.rule.description}"
        case MaintenanceStatus.UNKNOWN:
            return f"{check.status.value}: {check.rule.description} — no service history recorded"


def get_remaining(check: MaintenanceCheck, current_mileage_km: int):
    if check.next_due_km is not None:
        return f"{check.next_due_km - current_mileage_km} km remaining"
    else: 
        return f"{(check.next_due_date - date.today()).days} days remaining"
    
def run_menu(vehicle: Vehicle) -> None:
    while True:
        print("1) Add a service record")
        print("2) Add a maintenance rule")
        print("3) View service history")
        print("4) Check maintenance status")
        print("5) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            record = create_service_record_interactively()
            vehicle.add_service_record(record)
        elif choice == "2":
            rule = create_maintenance_rule_interactively()
            vehicle.add_maintenance_rule(rule)
        elif choice == "3":
            for record in sorted(vehicle.service_records, key=lambda r: r.date):
                print(record)
        elif choice == "4":
            for rule in vehicle.maintenance_rules:
                check = check_maintenance(rule, vehicle)
                print(format_maintenance_check(check, vehicle.mileage_km))
        elif choice == "5":
            break
        else:
            print("Not a valid option, try again.")