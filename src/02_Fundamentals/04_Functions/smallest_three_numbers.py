def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    return b if b <= c else c
    
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(smallest(a, b, c))

if __name__ == "__main__":
    main()