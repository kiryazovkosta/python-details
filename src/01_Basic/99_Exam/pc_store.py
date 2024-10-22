processors_price = float(input())
videocard_price = float(input())
ram_price = float(input())
ram_count = int(input())
discount = float(input())

processors_price_lv = processors_price * 1.57
videocard_price_lv = videocard_price * 1.57
ram_price_lv = ram_price * 1.57
total_ram_price = ram_price_lv * ram_count
processors_price_lv -= processors_price_lv * discount
videocard_price_lv -= videocard_price_lv * discount

total = processors_price_lv + videocard_price_lv + total_ram_price
print(f"Money needed - {total:.2f} leva.")