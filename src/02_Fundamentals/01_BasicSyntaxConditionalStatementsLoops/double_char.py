while True:
    text = input()
    if text == "End":
        break

    if text == "SoftUni":
        continue

    for char in text:
        print(f"{char}{char}", end="")
    print()