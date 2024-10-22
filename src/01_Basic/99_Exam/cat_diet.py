fats = int(input())
proteins = int(input())
carbo = int(input())
calories = int(input())
water = int(input())

f = (calories * (fats/100))/9
p = (calories * (proteins/100))/4
c = (calories * (carbo/100))/4

food = f + p + c
calories_per_gram = calories / food

calories_per_gram -= calories_per_gram * (water/100)

print(f"{calories_per_gram:.4f}")