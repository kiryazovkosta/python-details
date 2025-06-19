from project.devices.base_device import BaseDevice
from project.devices.laptop import Laptop
from project.devices.smartphone import Smartphone
from project.devices.smartwatch import Smartwatch
from project.repair_shop import RepairShop

class TechServiceManager:
    VALID_TYPES = ["Laptop", "Smartphone", "Smartwatch"]

    def __init__(self):
       self.devices = []
       self.repair_shops: list[RepairShop] = []

    def add_device(self, device_type: str, serial_number: str, durability: int, is_functional: bool):
        if device_type not in self.VALID_TYPES:
            raise ValueError("Invalid device type!")

        device_class = Laptop if device_type == self.VALID_TYPES[0] else Smartphone if device_type == self.VALID_TYPES[1] else Smartwatch
        device = device_class(serial_number, durability, is_functional)
        device.check_functionality()
        self.devices.append(device)
        return f"{device_type} is successfully added."

    def add_repair_shop(self, name: str, device_types: tuple):
        if not any(dt in self.VALID_TYPES for dt in device_types):
            raise ValueError("No valid device type!")

        shop = RepairShop(name, device_types)
        self.repair_shops.append(shop)
        return f"{name} is successfully added as a repair shop."

    def send_for_repair(self, repair_shop_name: str, device_type: str):
        shop = next((s for s in self.repair_shops if s.name == repair_shop_name), None)

        if device_type not in shop.device_types:
            return "The shop cannot repair this device type."

        device = next((d for d in self.devices if d.device_type == device_type and not d.is_functional), None)
        if not device:
            return f"There is no {device_type} that needs repair."

        self.devices.remove(device)
        shop.pending_devices.append(device)
        return f"{device.serial_number} was sent for repair to {repair_shop_name}."

    @staticmethod
    def process_repairs(repair_shop: RepairShop):
        return repair_shop.repair()

    def receive_repaired_devices(self, repair_shop: RepairShop):
        count = len(repair_shop.repaired_devices)
        self.devices.extend(repair_shop.repaired_devices)
        repair_shop.repaired_devices = []
        return f"Received {count} repaired devices."

    def tech_service_status(self):
        functional = len([d for d in self.devices if d.is_functional])
        malfunctioning = len([d for d in self.devices if not d.is_functional])
        result = [f"***Tech Service***",
                  f"Total number of functional devices: {functional}",
                  f"Total number of malfunctioning devices: {malfunctioning}",
                  f"Repair shops count: {len(self.repair_shops)}"]
        for shop in sorted(self.repair_shops, key=lambda x: x.name):
            result.append(f"@{shop.status()}")
        return "\n".join(result)