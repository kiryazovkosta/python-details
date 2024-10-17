def drink_by_ages(ages: int) -> str:
    if ages <= 14:
        return "toddy"
    elif ages <= 18:
        return  "coke"
    elif ages <= 21:
        return "beer"
    else:
        return "whisky"

def main():
    ages = int(input())
    print(f"drink {drink_by_ages(ages)}")

if __name__ == "__main__":
    main()