SQUARE_METER_PRICE = 7.61
DISCOUNT = 18
square_meters = float(input())

final_price = square_meters * SQUARE_METER_PRICE
discount_price = final_price * (DISCOUNT / 100)

print(f'The final price is {final_price - discount_price} lv.')
print(f'The discount is: {discount_price} lv.')

