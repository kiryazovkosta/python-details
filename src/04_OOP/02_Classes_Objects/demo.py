# class Person:
#     country = "Bulgaria"
#
#     def __init__(self, name: str, ages: int):
#         self.name = name
#         self.ages = ages
#
#     def __str__(self):
#         return f'{{\n\t"Person": {{\n\t\t"name": "{self.name}",\n\t\t"person": "{self.ages}" \n\t}} \n}}'
#
#     def greet(self):
#         print(f"Hello, I am {self.name} and I am {self.ages} years old.")
#
#     def celebrate_birthday(self):
#         self.ages += 1
#
#     def __add__(self, other):
#         return self.ages + other.ages
#
# person = Person("Kosta Kiryazov", 46)
# other_person = Person("Ivan Ivanov", 40)
# print(person)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"

point = Point(2, 4)
print(point)
point.set_x(3)
point.set_y(5)
print(point)
