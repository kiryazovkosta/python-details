def kwargs_length(**kwargs):
    return len(kwargs)

d = { 'name': 'Kosta', 'age': 46 }

print(kwargs_length(**d))