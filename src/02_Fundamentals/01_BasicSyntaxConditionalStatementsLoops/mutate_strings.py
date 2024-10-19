first = input()
second = input()

replaced = first
for i in range(len(first)):
    if first[i] == second[i]:
        continue

    replaced = replaced[: i] + second[i] + replaced[i + 1:]
    print(replaced)