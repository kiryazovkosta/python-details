from math import floor, ceil

def main():
    days = int(input())
    food = int(input())
    dog_daily_food = float(input())
    cat_daily_food = float(input())
    tortoise_daily_food = float(input()) / 1000

    eaten_food = dog_daily_food * days + cat_daily_food * days + tortoise_daily_food * days
    difference = food - eaten_food
    if difference >= 0:
        print(f"{floor(difference)} kilos of food left.")
    else:
        print(f"{ceil(abs(difference))} more kilos of food are needed.")

if __name__ == "__main__":
    main()