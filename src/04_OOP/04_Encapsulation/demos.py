# class Circle:
#     def __init__(self, r):
#         self.r = r
#         self.pi = 3.14
#
# c = Circle(8)
# print(c.r)
# print(c.pi)
# c.r = -10
# c.pi = 1.25
# print(c.r)
# print(c.pi)

# class Circle:
#     def __init__(self, r):
#         self.r = r
#         self.__pi = 3.14 #private
#         self._angle = 90 # protected
#
#     def check(self) -> bool:
#         return self.__pi == 3.14
#
# c = Circle(8)
# print(c.r)
# # print(c.__pi)
# c.r = -10
# c.__pi = 1.25
# print(c.r)
# print(c._Circle__pi)
# c._Circle__pi = 1.25
# print(c._Circle__pi)
# print(c._angle)
# c._angle = 5
# print(c._angle)

class Person:
    def __init__(self, name: str, age = 0):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age: int):
        if new_age < 0 or new_age > 120:
            raise ValueError("Invalid age value")
        self.__age = new_age

p = Person('Ivo', 5)
print(p.age)
p.age = 121
print(p.age)