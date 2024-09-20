pages_number = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours = pages_number / pages_per_hour
daily_hours = int(total_hours / days)
print(daily_hours)