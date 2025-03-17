from project.cat import Cat

class Kitten(Cat):
    DEFAULT_GENDER = "Female"
    def __init__(self, name :str, age: int):
        super().__init__(name, age, Kitten.DEFAULT_GENDER)

    def make_sound(self):
        return "Meow"