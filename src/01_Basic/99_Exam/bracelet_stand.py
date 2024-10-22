daily = float(input())
income = float(input())
outgo = float(input())
gif = float(input())

total_daily = 5 * daily
total_income = 5 * income

total = total_daily + total_income - outgo
diff = total - gif
if diff >= 0:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {abs(diff):.2f} BGN.")