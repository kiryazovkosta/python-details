number = int(input())

arr = []
while number > 0:
    arr.append(number % 10)
    number //= 10

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("".join(map(str, arr)))

