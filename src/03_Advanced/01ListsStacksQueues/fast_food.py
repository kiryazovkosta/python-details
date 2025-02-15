from collections import deque

food_quantity = int(input())
orders = deque([int(o) for o in input().split()])

print(max(orders))
while orders and orders[0] <= food_quantity:
    order = orders.popleft()
    food_quantity -= order

if orders:
    print("Orders left:", *orders)
else:
    print("Orders complete")