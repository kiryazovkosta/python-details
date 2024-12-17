notes = [0] * 10

while True:
    operation = input()
    if operation == "End":
        break

    index, task = operation.split("-")
    index = int(index) - 1
    notes[index] = task

tasks = [note for note in notes if note != 0]
print(tasks)