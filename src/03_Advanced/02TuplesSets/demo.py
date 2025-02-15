from collections import deque
#
# d = deque([1, 2, 3, 4, 5])
# print(d)
# d.rotate(-1)
# print(d)

count = 5
s = deque([1, 2, 3, 4, 5])
for _ in range(count + 1):
    print(s)
    s.append(s.popleft())