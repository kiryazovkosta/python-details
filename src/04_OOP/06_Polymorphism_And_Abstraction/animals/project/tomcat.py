from project.cat import Cat

class Tomcat(Cat):
    DEFAULT_GENDER = "Male"
    def __init__(self, name :str, age: int):
        super().__init__(name, age, Tomcat.DEFAULT_GENDER)

    def make_sound(self):
        return "Hiss"