guests = int(input())
guest_price = float(input())
budget = float(input())

if 10 <= guests <= 15:
    guest_price -= guest_price * 0.15
elif 15 < guests <= 20:
    guest_price -= guest_price * 0.20
elif guests > 25:
    guest_price -= guest_price * 0.25

cake_price = budget * 0.1
total_price = guests * guest_price + cake_price
if budget >= total_price:
    print(f"It is party time! {budget - total_price:.2f} leva left.")
else:
    print(f"No party! {abs(total_price - budget):.2f} leva needed.")