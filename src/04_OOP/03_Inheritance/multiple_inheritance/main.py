from project.employee import Employee
from project.person import Person
from project.teacher import Teacher

p = Person()
print(f"{type(p).__name__}:  {p.sleep()}")

e = Employee()
print(f"{type(e).__name__}:  {e.get_fired()}")

t = Teacher()
print(f"{type(t).__name__}:  {t.sleep()}")
print(f"{type(t).__name__}:  {t.get_fired()}")
print(f"{type(t).__name__}:  {t.teach()}")