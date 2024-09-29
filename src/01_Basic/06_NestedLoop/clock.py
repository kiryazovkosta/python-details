MAX_HOURS = 23
MAX_MINUTES = 59

for hour in range(0, MAX_HOURS + 1):
    for minutes in range(0, MAX_MINUTES + 1):
        print(f"{hour}:{minutes}")