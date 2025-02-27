from project.animal import Animal
from project.cat import Cat
from project.dog import Dog

a = Animal()
print(f"{type(a).__name__}: {a.eat()}")

d = Dog()
print(f"{type(d).__name__}: {d.eat()}")
print(f"{type(d).__name__}: {d.bark()}")

c = Cat()
print(f"{type(c).__name__}: {c.eat()}")
print(f"{type(c).__name__}: {c.meow()}")