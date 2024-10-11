

def read_input():
    budget = float(input())
    season = input()
    return budget, season

def get_car_type(budget: float):
    if budget > 500:
        return "Luxury class"
    elif 100 < budget <= 500:
        return "Compact class"
    else:
        return "Economy class"
    
def get_car_and_price(budget: float, season: str):
    if budget > 500:
        return "Jeep", budget * 0.90
    elif 100 < budget <= 500:
        if season == "Summer":
            return "Cabrio", budget * 0.45
        return "Jeep", budget * 0.80
    else:
        if season == "Summer":
            return "Cabrio", budget * 0.35
        return "Jeep", budget * 0.65
    
def print_output(car_type, car, price):
    print(car_type)
    print(f"{car} - {price:.2f}")

def main():
    budget, season = read_input()
    car_type = get_car_type(budget)
    car, price = get_car_and_price(budget, season)
    print_output(car_type, car, price)

if __name__ == "__main__":
    main()