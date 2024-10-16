def get_max(a, b, c) -> int:
    if a > b and a > c:
        return a
    else:
        if b > c:
            return b
    return c

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    m = get_max(a, b, c)
    print(m)

if __name__ == "__main__":
    main()