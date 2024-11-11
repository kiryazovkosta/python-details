peoples = [int(p) for p in input().split(" ")]
step = int(input())
excluded = []

index = 0
current_step = 1
while len(peoples) > 0:
    if index >= len(peoples):
        index = 0

    if current_step == step:
        #print(peoples[index])
        excluded.append(peoples[index])
        peoples.remove(peoples[index])
        current_step = 1
        #print(peoples)
        index -= 1
    else:
        current_step += 1

    index += 1

print(f"[{','.join(str(n) for n in excluded)}]")