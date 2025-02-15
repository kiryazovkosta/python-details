from collections import deque
kids = deque(input().split(" "))
n = int(input()) - 1
while len(kids) > 1:
    kids.rotate(-n)
    kid = kids.popleft()
    print(f"Removed {kid}")

last_kid = kids.pop()
print(f"Last is {last_kid}")