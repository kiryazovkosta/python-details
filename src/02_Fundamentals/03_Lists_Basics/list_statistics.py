positive = []
negative = []

n = int(input())
for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}\nSum of negatives: {sum(negative)}")