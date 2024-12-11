int_multiply = lambda number: number * 2
float_multiply = lambda number: number * 1.5
surround = lambda string: f"${string}$"

def operate(type_is: str, value: str) -> None:
    if type_is == "int":
        print(int_multiply(int(value)))
    elif type_is == "real":
        print(f"{float_multiply(float(value)):.2f}")
    else:
        print(surround(value))

type_is = input()
value = input()

operate(type_is, value)