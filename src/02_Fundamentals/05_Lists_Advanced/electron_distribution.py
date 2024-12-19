max_size = int(input())
n = 1
records = []
while True:
    size = 2 * n ** 2
    if size > max_size:
        records.append(max_size)
        break
    records.append(size)
    n += 1
    max_size -= size
    if max_size <= 0:
        break
print(records)