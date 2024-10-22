def convert(pounds: int):
    return pounds * 1.31

def main():
    pounds = int(input())
    usd = convert(pounds)
    print(f"{usd:.3f}")

if __name__ == "__main__":
    main()