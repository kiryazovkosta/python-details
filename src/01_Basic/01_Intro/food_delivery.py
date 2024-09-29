CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15
DESSERT_PRICE = 0.2
DELIVERY_PRICE = 2.5

chicken_menus_count = int(input())
fish_menus_count = int(input())
vegan_menus_count = int(input())

total_menu_price = (chicken_menus_count * CHICKEN_MENU + fish_menus_count * FISH_MENU + vegan_menus_count * VEGAN_MENU)
dessert_price = total_menu_price * DESSERT_PRICE
total_price = total_menu_price + dessert_price + DELIVERY_PRICE
print(total_price)