def age_assignment(*args, **kwargs):
    peoples = {}
    for name in args:
        peoples[name] = kwargs[name[0]]

    peoples = sorted(peoples.items())
    return "\n".join([f"{n} is {y} years old." for n, y in peoples])


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))