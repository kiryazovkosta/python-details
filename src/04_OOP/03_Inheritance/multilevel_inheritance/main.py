from project.car import Car
from project.sports_car import SportsCar
from project.vehicle import Vehicle

v = Vehicle()
print(f"{type(v).__name__}: {v.move()}")

c = Car()
print(f"{type(c).__name__}: {c.move()}")
print(f"{type(c).__name__}: {c.drive()}")

sc = SportsCar()
print(f"{type(sc).__name__}: {sc.move()}")
print(f"{type(sc).__name__}: {sc.drive()}")
print(f"{type(sc).__name__}: {sc.race()}")