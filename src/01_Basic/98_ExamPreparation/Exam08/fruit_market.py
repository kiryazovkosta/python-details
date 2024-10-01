strawberries_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberries_price = strawberries_price * 0.5
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

total_price = (strawberries_price * strawberries
               + raspberries * raspberries_price
               + oranges * oranges_price
               + bananas * bananas_price)
print(f"{total_price:.2f}")

