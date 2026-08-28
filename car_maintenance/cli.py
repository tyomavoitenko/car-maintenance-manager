from datetime import date

from car_maintenance.maintenance_category import MaintenanceCategory
from car_maintenance.maintenance_check import (
    MaintenanceCheck,
    MaintenanceStatus,
    check_maintenance,
)
from car_maintenance.maintenance_rule import (
    InvalidMaintenanceRuleError,
    MaintenanceRule,
)
from car_maintenance.service_record import ServiceRecord
from car_maintenance.vehicle import Vehicle


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


def prompt_date(message: str) -> date:
    while True:
        raw = input(message)
        try:
            return date.fromisoformat(raw)
        except ValueError:
            print("Please enter a valid date (yyyy-mm-dd).")


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


def create_vehicle_interactively() -> Vehicle | None:
    print("\nWelcome to Car Maintenance Manager 🚗\nTo add a vehicle enter its details below 👇\n")
    while True:
        try:
            manufacturer = input("Manufacturer: ")
            model = input("Model: ")
            year = prompt_int("Year: ")
            engine = input("Engine: ")
            mileage_km = prompt_int("Mileage: ")

            return Vehicle(
                manufacturer=manufacturer,
                model=model,
                year=year,
                engine=engine,
                mileage_km=mileage_km,
            )
        except (KeyboardInterrupt, EOFError):
            break


def create_service_record_interactively() -> ServiceRecord:
    print("Enter the service record details below 👇\n")
    category = prompt_category()
    mileage_km = prompt_int("Mileage (km): ")
    service_date = prompt_date("Date (yyyy-mm-dd): ")

    return ServiceRecord(
        date=service_date,
        mileage_km=mileage_km,
        category=category,
    )


def create_maintenance_rule_interactively() -> MaintenanceRule:
    print("Enter the maintenance rule details below 👇\n")
    while True:
        try:
            category = prompt_category()
            interval_km = prompt_optional_int("Interval (km): ")
            interval_month = prompt_optional_int("Interval (months): ")

            return MaintenanceRule(
                category=category,
                interval_km=interval_km,
                interval_months=interval_month,
            )
        except InvalidMaintenanceRuleError:
            print("Invalid rule (make sure you specify an interval). Try again.")


def format_maintenance_check(check: MaintenanceCheck, current_mileage_km: int):
    match check.status:
        case MaintenanceStatus.OK | MaintenanceStatus.DUE_SOON:
            return f"{check.status.value}: {check.rule.category.value} — {get_remaining(check, current_mileage_km)}"
        case MaintenanceStatus.OVERDUE:
            return f"{check.status.value}: {check.rule.category.value}"
        case MaintenanceStatus.UNKNOWN:
            return f"{check.status.value}: {check.rule.category.value} — no service history recorded"


def get_remaining(check: MaintenanceCheck, current_mileage_km: int) -> str:
    if check.next_due_km is not None:
        return f"{check.next_due_km - current_mileage_km} km remaining"
    assert check.next_due_date is not None
    return f"{(check.next_due_date - date.today()).days} days remaining"
    
    
def run_menu(vehicle: Vehicle) -> None:
    print(f"\nYour vehicle: {vehicle}")
    while True:
        print("\n1) Update current mileage")
        print("2) Check maintenance status")
        print("3) Add a service record")
        print("4) Add a maintenance rule")
        print("5) View service history")
        print("6) Exit\n")

        try:
            choice = input("Choose an option: ")
            match choice:
                case "1":
                    while True:
                        new_mileage = prompt_int("Current mileage: ")
                        if new_mileage >= vehicle.mileage_km:
                            vehicle.update_mileage(new_mileage)
                            break
                        else: 
                            print(f"Mileage can't decrease — your car's current reading is {vehicle.mileage_km:,} km.")
                case "2":
                    if vehicle.maintenance_rules:
                        for rule in vehicle.maintenance_rules:
                            check = check_maintenance(rule, vehicle)
                            print(format_maintenance_check(check, vehicle.mileage_km))
                    else:
                        print("Please add a maintenance rule first.")
                case "3":
                    record = create_service_record_interactively()
                    vehicle.add_service_record(record)
                case "4":
                    rule = create_maintenance_rule_interactively()
                    vehicle.add_maintenance_rule(rule)
                case "5":
                    if vehicle.service_records:
                        for record in sorted(vehicle.service_records, key=lambda r: r.date):
                            print(record)
                    else:
                        print("No service history recorded.")
                case "6":
                    break
                case _:
                    print("Not a valid option, try again.")
        except (KeyboardInterrupt, EOFError):
            break