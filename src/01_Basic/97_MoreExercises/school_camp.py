def main():
    season = input()
    group_type = input()
    students = int(input())
    nights = int(input())

    price_per_night, sport = get_price_and_sport(season, group_type)
    total_price = students * price_per_night * nights
    total_price = apply_discount(students, total_price)

    print(f"{sport} {total_price:.2f} lv.")

def get_price_and_sport(season, group_type):
    if group_type == "boys":
        return get_for_boys(season)
    elif group_type == "girls":
        return get_for_girls(season)
    else:
        return get_for_mixed(season)

def get_for_mixed(season):
    if season == "Winter":
        price_per_night = 10.00
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.50
        sport = "Cycling"
    else:
        price_per_night = 20.00
        sport = "Swimming"
    return price_per_night,sport

def get_for_girls(season):
    if season == "Winter":
        price_per_night = 9.60
        sport = "Gymnastics"
    elif season == "Spring":
        price_per_night = 7.20
        sport = "Athletics"
    else:
        price_per_night = 15.00
        sport = "Volleyball"
    return price_per_night,sport

def get_for_boys(season):
    if season == "Winter":
        price_per_night = 9.60
        sport = "Judo"
    elif season == "Spring":
        price_per_night = 7.20
        sport = "Tennis"
    else:
        price_per_night = 15.00
        sport = "Football"
    return price_per_night, sport

def apply_discount(students, total_price):
    if students >= 50:
        total_price -= total_price * 0.50
    elif 20 <= students < 50:
        total_price -= total_price * 0.15
    elif 10 <= students < 20:
        total_price -= total_price * 0.05
    
    return total_price

if __name__ == "__main__":
    main()