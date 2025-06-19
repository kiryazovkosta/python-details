from abc import ABC, abstractmethod

class BaseDevice(ABC):
    def __init__(self, serial_number: str, durability: int, is_functional: bool, device_type: str):
        self.serial_number = serial_number
        self.durability  = durability
        self.is_functional = is_functional
        self.device_type = device_type

    @property
    def serial_number(self):
        return self.__serial_number
    @serial_number.setter
    def serial_number(self, value):
        if not value.isalnum():
            raise ValueError("Invalid serial number!")
        self.__serial_number = value
    
    @property
    def durability (self):
        return self.__durability
    @durability .setter
    def durability (self, value):
        if value < 1 or value > 100:
            raise ValueError("Durability is out of range!")
        self.__durability = value

    @property
    def is_functional(self):
        return self.__is_functional
    @is_functional.setter
    def is_functional(self, value):
        self.__is_functional = value
    
    @property
    def device_type(self):
        return self.__device_type
    @device_type.setter
    def device_type(self, value):
        value = value.strip()
        if not value:
            raise ValueError("Type cannot be empty!")
        self.__device_type = value

    def check_functionality(self):
        if self.is_functional and self.durability < 2:
            self.is_functional = False

    @abstractmethod
    def repair(self):
        pass