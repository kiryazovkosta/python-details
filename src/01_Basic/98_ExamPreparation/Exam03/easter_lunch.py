KOSUNAC_PRICE = 3.20
EGG_PRICE = 4.35
COOKIE_PRICE = 5.40
PAINT_PRICE = 0.15
EGGS_IN_PACK = 12

kosunacs = int(input())
eggs = int(input())
cookies = int(input())

kozunacs_price = kosunacs * KOSUNAC_PRICE
eggs_price = eggs * EGG_PRICE
cookies_price = cookies * COOKIE_PRICE
paint_price = eggs * EGGS_IN_PACK * PAINT_PRICE

price = kozunacs_price + eggs_price + cookies_price + paint_price
print(f"{price:.2f}")