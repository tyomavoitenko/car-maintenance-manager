from car_maintenance import cli, storage

try:
    vehicle = storage.load_vehicle("data/vehicle.json")
except FileNotFoundError:
    vehicle = cli.create_vehicle_interactively()

if vehicle is not None:
    cli.run_menu(vehicle)
    storage.save_vehicle(vehicle, path="data/vehicle.json")