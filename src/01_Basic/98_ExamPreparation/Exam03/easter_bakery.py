flour_price = float(input())
flour = float(input())
sugar = float(input())
eggs = int(input())
yeast = int(input())

sugar_price = flour_price - (flour_price * 0.25)
eggs_price = flour_price + flour_price * 0.1
yeast_price = sugar_price - sugar_price * 0.8

total = flour * flour_price + sugar * sugar_price + eggs * eggs_price + yeast * yeast_price
print(f"{total:.2f}")