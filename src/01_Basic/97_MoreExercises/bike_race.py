RACE_TAX = {
    "juniors": {"trail": 5.50, "cross-country": 8, "downhill": 12.25, "road": 20 },
    "seniors": {"trail": 7, "cross-country": 9.50, "downhill": 13.75, "road": 21.50 },
}

def read_input():
    return int(input()), int(input()), input()

def get_racer_tax(race_type: str):
    return RACE_TAX["juniors"][race_type], RACE_TAX["seniors"][race_type]

def main():
    juniors, seniors, race_type = read_input()
    junior_tax, senior_tax = get_racer_tax(race_type)
    if race_type == "cross-country" and juniors + seniors >= 50:
        junior_tax -= junior_tax * 0.25
        senior_tax -= senior_tax * 0.25
    income = juniors * junior_tax + seniors * senior_tax
    outcome = income * 0.05
    amount = income - outcome
    print(f"{amount:.2f}")

if __name__ == "__main__":
    main()