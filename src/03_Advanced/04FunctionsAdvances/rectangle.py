def rectangle(length: int, width: int)-> str:
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return  length * width

    def perimeter():
        return 2 * width + 2 * length

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"



print(rectangle(2, 10))

print(rectangle('2', 10))