def calc(operator: str, a: int, b: int) -> int:
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    else:
        raise SyntaxError("Invalid operator")

def main():
    oper = input()
    a = int(input())
    b = int(input())

    print(calc(oper, a, b))

if __name__ == "__main__":
    main()