words = [word for word in input().split(" ")]

while True:
    command = input().split(" ")
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        startIndex = int(command[1])
        endIndex = int(command[2])
        if 0 < startIndex > len(words) - 1:
            continue

        endIndex = len(words) - 1 if endIndex > len(words) else endIndex

        for _ in range(startIndex + 1, endIndex + 1):
            words[startIndex] += words[startIndex + 1]
            words.pop(startIndex + 1)
    elif command[0] == "divide":
        p = int(command[2])
        w = words[int(command[1])]
        l = len(w)
        parts = l // p
        sub = [w[index: index+parts] for index in range(0, p, parts)]
        sub[-1] += w[parts * p:]
        print(sub)

print(" ".join(words))