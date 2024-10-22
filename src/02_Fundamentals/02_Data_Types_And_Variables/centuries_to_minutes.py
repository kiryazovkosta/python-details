from math import floor

def convert(centrues: int):
    years = centrues * 100
    days = floor(years * 365.2422)
    hours = days * 24
    minutes = hours * 60
    return years, days, hours, minutes

def main():
    centrues = int(input())
    years, days, hours, minutes = convert(centrues)
    print(f"{centrues} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

main()