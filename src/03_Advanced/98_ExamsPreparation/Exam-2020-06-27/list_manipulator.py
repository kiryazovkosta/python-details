def list_manipulator(numbers: list[int], command: str, position: str, *args):
    if command == "add":
        if position == "beginning":
            numbers = list(args) + numbers
        elif position == "end":
            numbers.extend(args)
    elif command == "remove":
        count = args[0] if args else 1
        if position == "beginning":
            numbers = numbers[count:]
        elif position == "end":
            numbers = numbers[:-count] if count <= len(numbers) else []

    return numbers

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
