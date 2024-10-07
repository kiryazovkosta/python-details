hall_rent: float = float(input())

cake: float = hall_rent * 0.2
drinks: float = cake - cake * 0.45
animator: float = hall_rent / 3

total = hall_rent + cake + drinks + animator
print(total)