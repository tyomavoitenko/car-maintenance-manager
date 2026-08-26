import tests.helper as helper
import car_maintenance.storage as storage
from datetime import date

def test_write_and_read_file(tmp_path):
    vehicle = helper.get_vehicle()
    vehicle.add_maintenance_rule(helper.get_rule())
    vehicle.add_service_record(helper.get_service_record(200_000, date(2026, 1, 1)))

    file_path = tmp_path / "vehicle.json"
    storage.save_vehicle(vehicle, file_path)
    loaded_vehicle = storage.load_vehicle(file_path)

    assert vehicle == loaded_vehicle