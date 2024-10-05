SEASONS = {
    "Winter": {"Dubai": 45000, "Sofia": 17000 ,"London": 24000 },
    "Summer": {"Dubai": 40000, "Sofia": 12500 ,"London": 20250 }
}

def get_daily_price(season, destination):
    return SEASONS[season][destination]

def calculate_discount(destination, final_price):
    if destination == "Dubai":
        final_price -= final_price * 0.3
    elif destination == "Sofia":
        final_price += final_price * 0.25
    return final_price

def print_result(budget, final_price):
    diff = budget - final_price
    if diff >= 0:
        print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
    else:
        print(f"The director needs {abs(diff):.2f} leva more!")

def main():
    budget = float(input())
    destination = input()
    season = input()
    days = int(input())

    daily_price = get_daily_price(season, destination)
    final_price = days * daily_price
    final_price = calculate_discount(destination=destination, final_price=final_price)
    print_result(budget, final_price)

if __name__ == "__main__":
    main()
