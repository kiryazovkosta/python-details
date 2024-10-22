def meters_to_km(meters):
    return meters / 1000

def main():
    meters = int(input())
    print(f"{meters_to_km(meters=meters):.2f}")

if __name__ == "__main__":
    main()