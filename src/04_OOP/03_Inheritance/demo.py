class Person:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def eat(self):
        return "eating"

    def get_person(self):
        return f"{self.name} -> {self.age}"

class Teacher(Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary

# class Fireman:
#     def __init__(self, name: str, age: int, salary: int, equipment: str):
#         self.salary = salary
#         self.age = age
#         self.name = name
#         self.equipment = equipment
#
#     def eat(self):
#         return "eating"

t = Teacher('name', 25, 12000)
t.eat()

class Student(Person):
    pass

s = Student('student', 35)
print(s.get_person())
print(s.__str__())