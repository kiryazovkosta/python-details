VIP_PRICE = 499.99
NORMAL_PRICE = 249.99

def read_input():
    budget = float(input())
    ticket_type = input()
    persons = int(input())
    return budget, ticket_type, persons

def calc_transport(persons, budget):
    if 1 <= persons <= 4:
        return  budget * 0.75
    elif 5 <= persons <= 9:
        return  budget * 0.60
    elif 10 <= persons <= 24:
        return  budget * 0.50
    elif 25 <= persons <=49:
        return  budget * 0.40
    else:
        return  budget * 0.25

def calc_tickets_price(persons, ticket_type):
    if ticket_type == "VIP":
        return persons * VIP_PRICE
    elif ticket_type == "Normal":
        return persons * NORMAL_PRICE
    
def print_output(budget, outcome):
    diff = budget - outcome
    if diff >= 0:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {abs(diff):.2f} leva.")

def main():
    budget, ticket_type, persons = read_input()
    transport = calc_transport(persons=persons, budget=budget)
    tickets_price = calc_tickets_price(persons, ticket_type)
    outcome = transport + tickets_price
    print_output(budget, outcome)

if __name__ == "__main__":
    main()