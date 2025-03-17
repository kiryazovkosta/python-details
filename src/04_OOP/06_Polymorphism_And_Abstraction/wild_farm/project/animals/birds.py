from project.animals.animal import Bird
from project.food import Meat, Vegetable, Food


class Owl(Bird):
    FOOD_WEIGHT = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Owl.FOOD_WEIGHT

class Hen(Bird):
    FOOD_WEIGHT = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.FOOD_WEIGHT