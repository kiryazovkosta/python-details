def chars_in_range(start: str, end: str):
    return [chr(n) for n in range(ord(start) + 1, ord(end))]

def main():
    a = input()
    b = input()
    symbols = chars_in_range(a, b)
    print(" ".join(symbols))

if __name__ == "__main__":
    main()