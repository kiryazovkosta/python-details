first = {int(n) for n in input().split()}
second = set([int(n) for n in input().split()])

for _ in range(int(input())):
    command = input().split()
    operation = command[0]
    collection = command[1]
    numbers = [int(n) for n in command[2:]]

    if operation == "Add":
        if collection == "First":
            first.update(numbers)
        else:
            second.update(numbers)
    elif operation == "Remove":
        if collection == "First":
            first.difference_update(numbers)
        else:
            second.difference_update(numbers)
    else:
        print(first.issubset(second) or second.issubset(first))

print(', '.join(map(str, sorted(first))))
print(*sorted(second), sep=", ")
