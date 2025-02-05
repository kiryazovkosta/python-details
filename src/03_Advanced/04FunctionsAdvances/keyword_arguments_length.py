def kwargs_length(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}->{value}->{type(value)}")
    return len(kwargs)

d = { 'name': 'Kosta', 'age': 46, 'city': { 'name': 'New York', 'Code': 8200 }, 'location': 23.130 }

print(kwargs_length(**d))
print(kwargs_length(**{}))