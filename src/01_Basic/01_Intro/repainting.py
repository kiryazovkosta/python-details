PLASTIC_SHEET_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
ADDED_PAINT = 0.1
ADDED_PLASTIC_SHEET = 2
BAGS_PRICE = 0.40
WORKING_PRICE_PER_HOUR = 0.3

plastic_sheet = int(input())
paint = int(input())
paint_thinner = int(input())
working_hours = int(input())

total_material_price = (((plastic_sheet + ADDED_PLASTIC_SHEET) * PLASTIC_SHEET_PRICE)
                        + (paint * PAINT_PRICE + (paint * PAINT_PRICE * ADDED_PAINT))
                        + (paint_thinner * PAINT_THINNER_PRICE)
                        + BAGS_PRICE)
price_per_hour = total_material_price * WORKING_PRICE_PER_HOUR
total_price = total_material_price + (working_hours * price_per_hour)
print(total_price)
