while True:
    name = input()
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    name_len = len(name)
    if name_len < 5:
        print(f"{name} goes to Gryffindor.")
    elif name_len == 5:
        print(f"{name} goes to Slytherin.")
    elif name_len == 6:
        print(f"{name} goes to Ravenclaw.")
    elif name_len > 6:
        print(f"{name} goes to Hufflepuff.")