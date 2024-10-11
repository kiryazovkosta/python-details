hrizantemi = int(input())
rosi = int(input())
laleta = int(input())
season = input()
is_holiday = input()

if season == "Spring" or season == "Summer":
    hrizantemi_price = 2.00
    rozi_price = 4.10
    laleta_price = 2.50
else:
    hrizantemi_price = 3.75
    rozi_price = 4.50
    laleta_price = 4.15

if is_holiday == "Y":
    hrizantemi_price += hrizantemi_price * 0.15
    rozi_price += rozi_price * 0.15
    laleta_price += laleta_price * 0.15

total = (
    hrizantemi * hrizantemi_price
    + rosi * rozi_price
    + laleta * laleta_price
)

if laleta > 7 and season == "Spring":
    total -= total * 0.05
if rosi >= 10 and season == "Winter":
    total -= total * 0.1
if hrizantemi + rosi + laleta > 20:
    total -= total * 0.2

total += 2
print(f"{total:.2f}")