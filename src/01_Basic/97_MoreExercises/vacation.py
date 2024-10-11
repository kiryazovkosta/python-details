def read_input():
    budget = float(input())
    season = input()
    return budget, season

def get_accommodation_type(budget: float):
    if budget > 3000:
        return "Hotel"
    elif 1000 < budget <= 3000:
        return "Hut"
    else:
        return "Camp"
    
def get_destination_and_price(budget: float, season: str):
    if budget > 3000:
        price = budget * 0.90
        if season == "Summer":
            return "Alaska", price
        else:
            return "Morocco", price
    elif 1000 < budget <= 3000:
        if season == "Summer":
            return "Alaska", budget * 0.80
        else:
            return "Morocco", budget * 0.60
    else:
        if season == "Summer":
            return "Alaska", budget * 0.65
        else:
            return "Morocco", budget * 0.45
        
def print_output(accommodation_type, destination, price):
    print(f"{destination} - {accommodation_type} - {price:.2f}")

def main():
    budget, season = read_input()
    accommodation_type = get_accommodation_type(budget)
    destination, price = get_destination_and_price(budget, season)
    print_output(accommodation_type, destination, price)

if __name__ == "__main__":
    main()