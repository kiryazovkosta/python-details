deposit_sum = float(input())
period = int(input())
annual_rate = float(input())

total_sum = deposit_sum + period * ((deposit_sum * (annual_rate/100) ) / 12)
print(total_sum)
