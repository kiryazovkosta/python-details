DISCOUNT_NIGHTS = 7
DISCOUNT_PERCENTAGES = 0.05

budget = float(input())
nights = int(input())
night_price = float(input())
extra_outgo = int(input())

if nights > DISCOUNT_NIGHTS:
    night_price -= night_price * DISCOUNT_PERCENTAGES

outgo = (nights * night_price) + (budget * extra_outgo/100)
diff = budget - outgo
if diff >= 0:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
        print(f"{abs(diff):.2f} leva needed.")