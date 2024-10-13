mens = int(input())
woman = int(input())
tables = int(input())

filledTables = 0
areFilled = False
for m in range(1, mens + 1):
    for w in range(1, woman + 1):
        if filledTables == tables:
            areFilled = True
            break
        print(f"({m} <-> {w})", end=" ")
        filledTables += 1
    if areFilled:
        break