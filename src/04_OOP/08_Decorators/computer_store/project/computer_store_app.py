from multiprocessing.managers import rebuild_as_list

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = None
        if type_computer == self.VALID_TYPES[0]:
            computer = DesktopComputer(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
        else:
            computer = Laptop(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((c for c in self.warehouse if c.processor == wanted_processor and c.price <= client_budget and c.ram >= wanted_ram), None)
        if computer is None:
            raise Exception("Sorry, we don't have a computer for you.")

        self.warehouse.remove(computer)
        self.profits += (client_budget - computer.price)
        return f"{computer.__repr__()} sold for {client_budget}$."

