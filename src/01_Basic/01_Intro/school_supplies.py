PENS_PACK_PRICE = 5.80
MARKERS_PACK_PRICE = 7.20
CLEANER_PRICE = 1.20

packs_pens = int(input())
packs_markers = int(input())
cleaner_liters = int(input())
discount = int(input())

total_pens_price = packs_pens * PENS_PACK_PRICE
total_markers_price = packs_markers * MARKERS_PACK_PRICE
total_cleaner_price = cleaner_liters * CLEANER_PRICE
discount_percentages = discount / 100

total_sum = total_pens_price + total_markers_price + total_cleaner_price
sum_with_discount = total_sum - (total_sum * discount_percentages)
print(sum_with_discount)