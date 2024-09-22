ROOM_FOR_ONE_PERSON_PRICE = 18.00
APARTMENT_PRICE = 25.00
PRESIDENT_APARTMENT_PRICE = 35.00

days = int(input())
room = input()
review = input()

nights = days - 1
total_price = 0.0

if nights < 10:
    if room == "room for one person":
        total_price = nights * ROOM_FOR_ONE_PERSON_PRICE
    elif room == "apartment":
        total_price = nights * APARTMENT_PRICE
        total_price -= total_price * 0.3
    else:
        total_price = nights * PRESIDENT_APARTMENT_PRICE
        total_price -= total_price * 0.1

elif 10 <= nights <= 15:
    if room == "room for one person":
        total_price = nights * ROOM_FOR_ONE_PERSON_PRICE
    elif room == "apartment":
        total_price = nights * APARTMENT_PRICE
        total_price -= total_price * 0.35
    else:
        total_price = nights * PRESIDENT_APARTMENT_PRICE
        total_price -= total_price * 0.15
else:
    if room == "room for one person":
        total_price = nights * ROOM_FOR_ONE_PERSON_PRICE
    elif room == "apartment":
        total_price = nights * APARTMENT_PRICE
        total_price -= total_price * 0.5
    else:
        total_price = nights * PRESIDENT_APARTMENT_PRICE
        total_price -= total_price * 0.2

if review == "positive":
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")