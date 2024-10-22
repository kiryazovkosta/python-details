weight = float(input())
service_type = input()
distance = int(input())

price_per_km = 0
if weight < 1:
    price_per_km = 0.03
elif 1 <= weight < 10:
    price_per_km = 0.05
elif 10 <= weight < 40:
    price_per_km = 0.10
elif 40 <= weight < 90:
    price_per_km = 0.15
elif 90 <= weight <= 150:
    price_per_km = 0.20

total_regular_price = distance * price_per_km

extra_price_per_km = 0
if service_type == "express":
    if weight < 1:
        extra_price_per_km = price_per_km * 0.8
    elif 1 <= weight < 10:
        extra_price_per_km = price_per_km * 0.4
    elif 10 <= weight < 40:
        extra_price_per_km = price_per_km * 0.05
    elif 40 <= weight < 90:
        extra_price_per_km = price_per_km * 0.02
    elif 90 <= weight <= 150:
        extra_price_per_km = price_per_km * 0.01

extra_weight_price = weight * extra_price_per_km
total_extra_price = distance * extra_weight_price

total = total_regular_price + total_extra_price
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total:.2f} lv.")