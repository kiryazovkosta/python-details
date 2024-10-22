computers = int(input())

total_sales = 0
total_rating = 0
for _ in range(computers):
    number = int(input())

    rating =  number % 10
    sales = number // 10

    total_rating += rating
    if rating == 2:
        sales = sales * 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 1
    total_sales += sales

print(f"{total_sales:.2f}")
print(f"{total_rating/computers:.2f}")