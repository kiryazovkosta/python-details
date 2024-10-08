vegetable_price = float(input())
fruit_price = float(input())
vegetables = int(input())
fruits = int(input())
total_price = vegetables * vegetable_price + fruits * fruit_price
total_price_in_euro = total_price / 1.94
print(f"{total_price_in_euro:.2f}")