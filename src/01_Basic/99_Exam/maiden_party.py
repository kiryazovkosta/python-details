girl_party_price = float(input())
letters = int(input())
roses = int(input())
keys = int(input())
memes = int(input())
surprises = int(input())

total_sum = letters * 0.6 + roses * 7.2 + keys * 3.6 + memes * 18.20 + surprises * 22
articuls = letters + roses + keys + memes + surprises
if articuls >= 25:
    total_sum -= total_sum * 0.35

total_sum -= total_sum * 0.1

diff = total_sum - girl_party_price
if diff >= 0:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {abs(diff):.2f} lv needed.")