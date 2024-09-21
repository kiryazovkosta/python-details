PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toys_count = puzzles + dolls + bears + minions + trucks
total_toys_price = (puzzles * PUZZLE_PRICE
                    + dolls * DOLL_PRICE
                    + bears * BEAR_PRICE
                    + minions * MINION_PRICE
                    + trucks * TRUCK_PRICE)
if total_toys_count >= 50:
    total_toys_price = total_toys_price - (total_toys_price * 0.25)

total_toys_price = total_toys_price - total_toys_price * 0.1

money = total_toys_price - trip_price
if money >= 0:
    print(f"Yes! {money:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money):.2f} lv needed.")

