concatenate = lambda a, b, c : f"{a}{b}{c}"

def main():
    a = input()
    b = input()
    c = input()
    string = concatenate(a, b, c)
    print(string)

if __name__ == "__main__":
    main()