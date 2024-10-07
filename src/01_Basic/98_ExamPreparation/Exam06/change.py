bitcoins = int(input())
uwans = float(input())
commision = float(input())

levs = bitcoins * 1168
dollars = uwans * 0.15
levs += dollars * 1.76
euro = levs/1.95
euro -= euro * commision/100
print(f"{euro:.2f}")