def calc_area(width, height):
    return width * height

def main():
    w = int(input())
    h = int(input())
    print(calc_area(w, h))

if __name__ == "__main__":
    main()