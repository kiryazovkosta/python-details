ROSE_PRICE = 5.00
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
DAFFODIL_PRICE = 3.00
GLADIOLUS_PRICE = 2.50

flower_type = input()
flowers_count = int(input())
budget = int(input())

total_amount = 0.0
if flower_type == "Roses":
    total_amount = flowers_count * ROSE_PRICE
    if flowers_count > 80:
        total_amount = total_amount - (total_amount * 0.1)
elif flower_type == "Dahlias":
    total_amount = flowers_count * DAHLIA_PRICE
    if flowers_count > 90:
        total_amount = total_amount - (total_amount * 0.15)
elif flower_type == "Tulips":
    total_amount = flowers_count * TULIP_PRICE
    if flowers_count > 80:
        total_amount = total_amount - (total_amount * 0.15)
elif flower_type == "Narcissus":
    total_amount = flowers_count * DAFFODIL_PRICE
    if flowers_count < 120:
        total_amount = total_amount + (total_amount * 0.15)
elif flower_type == "Gladiolus":
    total_amount = flowers_count * GLADIOLUS_PRICE
    if flowers_count < 80:
        total_amount = total_amount + (total_amount * 0.2)

balance = budget - total_amount
if balance >= 0:
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {balance:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(balance):.2f} leva more.")