TICKET_PRICES = {
    "john wick": {"drink": 12, "popcorn": 15, "menu": 19},
    "star wars": {"drink": 18, "popcorn": 25, "menu": 30},
    "jumanji": {"drink": 9, "popcorn": 11, "menu": 14}
}

def get_ticket_price(movie, package):
    movie = movie.lower()
    package = package.lower()
    return TICKET_PRICES[movie][package]

def calculate_discount(movie, tickets, final_price):
    movie = movie.lower()
    if movie == "star wars" and tickets >= 4:
        final_price -= final_price * 0.3
    elif movie == "jumanji" and tickets == 2:
        final_price -= final_price * 0.15
    return final_price

def main():
    movie = input()
    package = input()
    tickets = int(input())

    ticket_price = get_ticket_price(movie, package)
    final_price = tickets * ticket_price
    final_price = calculate_discount(movie, tickets, final_price)
    print(f"Your bill is {final_price:.2f} leva.")

if __name__ == "__main__":
    main()