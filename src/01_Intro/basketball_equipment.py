year_tax = int(input())

shoes_price = year_tax - (year_tax * 0.4)
uniform_price = shoes_price - (shoes_price * 0.2)
ball_price = uniform_price * 0.25
accessories_price = ball_price * 0.2
annual_fee = year_tax + shoes_price + uniform_price + ball_price + accessories_price
print(annual_fee)