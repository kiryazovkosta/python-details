months = int(input())
eSum = 0
oSum = 0

for _ in range(months):
    electricity_tax = float(input())
    eSum += electricity_tax
    oTax = (electricity_tax + 35) + (electricity_tax + 35) * 0.2
    oSum += oTax

total = eSum + oSum + months * 20 + months * 15
print(f"Electricity: {eSum:.2f} lv")
print(f"Water: {months * 20:.2f} lv")
print(f"Internet: {months * 15:.2f} lv")
print(f"Other: {oSum:.2f} lv")
print(f"Average: {total/months:.2f} lv")