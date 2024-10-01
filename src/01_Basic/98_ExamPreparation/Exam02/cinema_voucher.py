voucher_price = int(input())

movies_count = 0
other_count = 0

while voucher_price > 0:
    item = input()
    if item == "End":
        break

    is_movie = False
    item_len = len(item)
    item_price = 0
    if item_len > 8:
        is_movie = True
        item_price = ord(item[0]) + ord(item[1])
    else:
        item_price = ord(item[0])

    if voucher_price < item_price:
        break

    voucher_price -= item_price
    if is_movie:
        movies_count += 1
    else:
        other_count += 1

print(movies_count)
print(other_count)



