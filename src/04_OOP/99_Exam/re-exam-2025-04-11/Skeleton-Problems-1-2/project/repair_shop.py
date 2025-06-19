from project.devices.base_device import BaseDevice

class RepairShop:
    def __init__(self, name: str, device_types: tuple):
        self.name = name
        self.device_types = device_types
        self.pending_devices: list[BaseDevice] = []
        self.repaired_devices: list[BaseDevice] = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        stripped_value = value.strip()
        if len(stripped_value) < 2:
            raise ValueError("Invalid repair shop name!")
        self.__name = value

    @property
    def device_types(self):
        return self.__device_types
    @device_types.setter
    def device_types(self, value):
        if not value:
            raise ValueError("No device types provided!")
        self.__device_types = value

    def repair(self):
        count = len(self.pending_devices)
        for device in self.pending_devices[:]:
            device.repair()
            self.pending_devices.remove(device)
            self.repaired_devices.append(device)

        return f"Repaired {count} device/s."

    def status(self):
        return f"{self.name} has {len(self.pending_devices)} devices pending for repair and {len(self.repaired_devices)} devices repaired."

