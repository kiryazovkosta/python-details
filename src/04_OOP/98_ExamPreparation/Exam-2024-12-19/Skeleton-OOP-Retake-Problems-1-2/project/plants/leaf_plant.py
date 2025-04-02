from project.plants.base_plant import BasePlant

class LeafPlant(BasePlant):
    SIZES = ("S", "M", "L")

    def __init__(self, name: str, price: float, water_needed: int, size: str):
        super().__init__(name, price, water_needed)
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if value not in self.SIZES:
            raise ValueError("Size must be a valid one!")
        self.__size = value

    def plant_details(self) -> str:
        return (f"Leaf Plant: {self.name}, "
                f"Price: {self.price:.2f}, "
                f"Watering: {self.water_needed}ml, "
                f"Size: {self.size}")