a = int(input())
b = int(input())
operator = input()

result = 0.00
odd_or_even = ""

if operator in ["+", "-", "*"]:
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    else:
        result = a * b

    odd_or_even = "even" if result % 2 == 0 else "odd"
    print(f"{a} {operator} {b} = {result} - {odd_or_even}")
elif operator in ["/", "%"]:
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        if operator == "/":
            result = a / b
            print(f"{a} {operator} {b} = {result:.2f}")
        else:
            result = a % b
            print(f"{a} {operator} {b} = {result}")

