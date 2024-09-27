number = round(float(input()) * 100)
instead = int(number)

coins_number = 0

coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
i = 0
while instead > 0 and i < len(coin_values):
    coin = coin_values[i]
    if instead >= coin:
        coins_number += instead // coin
        instead %= coin
    i += 1

print(coins_number)

