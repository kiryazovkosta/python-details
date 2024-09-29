month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50.00
    apartment_price = 65.00
    if nights > 14:
        studio_price -= studio_price * 0.30
    elif nights > 7:
        studio_price -= studio_price * 0.05
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price -= studio_price * 0.2
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if nights > 14:
    apartment_price -= apartment_price * 0.1

studio_total_price = nights * studio_price
apartment_total_price = nights * apartment_price
print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")
