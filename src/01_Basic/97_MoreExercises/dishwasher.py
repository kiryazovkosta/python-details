DISH_QUANTITY = 5
POT_QUANTITY = 15
DETERGENT_QUANTITY = 750

class ChangeResult:
    def __init__(self, counter, detergent, dish_counter, pot_counter):
        self.counter = counter
        self.detergent = detergent
        self.dish_counter = dish_counter
        self.pot_counter = pot_counter

def main():
    bottles = int(input())
    result = ChangeResult(1, bottles * DETERGENT_QUANTITY, 0, 0)
    while True:
        command = input()
        if command == "End":
            print_success(result.detergent, result.dish_counter, result.pot_counter)
            break
        items = int(command)
        quantity = get_washed(items, result.counter)
        if quantity > result.detergent:
            print(f"Not enough detergent, {quantity - result.detergent} ml. more necessary!")
            break
        change_values(quantity, items, result)

def change_values(quantity, items, result: ChangeResult):
    result.detergent -= quantity
    if result.counter % 3 == 0:
        result.pot_counter += items
    else:
        result.dish_counter += items
    result.counter += 1

def get_washed(items, counter):
    if counter % 3 != 0:
        quantity = items * DISH_QUANTITY
    else:
        quantity = items * POT_QUANTITY
    return quantity

def print_success(detergent, dish_counter, pot_counter):
    print("Detergent was enough!")
    print(f"{dish_counter} dishes and {pot_counter} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")

if __name__ == "__main__":
    main()