from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat, Seed, Food


class Mouse(Mammal):
    FOOD_WEIGHT = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Mouse.FOOD_WEIGHT

class Dog(Mammal):
    FOOD_WEIGHT = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Dog.FOOD_WEIGHT

class Cat(Mammal):
    FOOD_WEIGHT = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, (Meat, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Cat.FOOD_WEIGHT

class Tiger(Mammal):
    FOOD_WEIGHT = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Tiger.FOOD_WEIGHT