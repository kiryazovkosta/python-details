from collections import deque

money = [int(n) for n in input().split()]
foods = deque([int(n) for n in input().split()])

food_count = 0
while money and foods:
    amount = money.pop()
    food = foods.popleft()
    if amount == food:
        food_count += 1
    elif amount > food:
        food_count += 1
        change = amount - food
        if money:
            money[-1] += change
        else:
            money.append(change)

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count > 1:
    print(f"Henry ate: {food_count} foods.")
elif food_count > 0:
    print(f"Henry ate: {food_count} food.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")

