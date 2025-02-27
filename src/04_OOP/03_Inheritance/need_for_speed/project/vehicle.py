class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel: float = fuel
        self.horse_power: int = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        used_fuel = kilometers * self.fuel_consumption
        if self.fuel >= used_fuel:
            self.fuel -= used_fuel