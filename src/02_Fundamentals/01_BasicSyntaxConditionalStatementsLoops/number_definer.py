def print_number(number: float) -> str:
    if number == 0:
        return "zero"
    if number > 0:
        if number > 1000000:
            return "large positive"
        elif number < 1:
            return "small positive"
        else:
            return "positive"
    else:
        if number < -100000:
            return "large negative"
        elif number > -1:
            return "small negative"
        else:
            return "negative"

def main():
    number = float(input())
    print(print_number(number))

if __name__ == "__main__":
    main()
