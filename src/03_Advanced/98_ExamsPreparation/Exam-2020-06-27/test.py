created = {
    "First" : 2,
    "Second": 1,
    "Next": 2,
    "Last": 3

}

xx = len([value for key, value in created.items() if value >= 3])
print(xx)