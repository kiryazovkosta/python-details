WELL_RESTING_TIME = 30000
holidays = int(input())
working_days = 365 - holidays
real_resting_time: int = holidays * 127 + working_days * 63
if real_resting_time < WELL_RESTING_TIME:
    diff = WELL_RESTING_TIME - real_resting_time
    print("Tom sleeps well")
    print(f"{diff // 60} hours and {diff % 60} minutes less for play")
else:
    diff = real_resting_time - WELL_RESTING_TIME
    print("Tom will run away")
    print(f"{diff // 60} hours and {diff % 60} minutes more for play")