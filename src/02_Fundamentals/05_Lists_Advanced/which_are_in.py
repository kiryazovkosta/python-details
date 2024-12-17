first = [word for word in input().split(", ")]
second = [word for word in input().split(", ")]

result = [pattern for pattern in first if any(word.find(pattern) >= 0 for word in second)]

print(result)