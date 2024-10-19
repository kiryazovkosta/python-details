actions_lower = ["coding", "dog", "cat", "movie" ]
actions_upper = ["CODING", "DOG", "CAT", "MOVIE" ]

coffee_counter = 0
while True:
    command = input()
    if command == "END":
        print(coffee_counter)
        break

    if command in actions_lower:
        coffee_counter += 1
    elif command in actions_upper:
        coffee_counter += 2

    if coffee_counter > 5:
        print("You need extra sleep")
        break