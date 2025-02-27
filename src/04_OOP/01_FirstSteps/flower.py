class Flower:
    def __init__(self, name: str, water_requirements: int, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            self.is_happy = True
        else:
            self.is_happy = False

    def status(self):
        status = "happy" if self.is_happy == True else "not happy"
        return f"{self.name} is {status}"

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
flower.water(60)
print(flower.status())