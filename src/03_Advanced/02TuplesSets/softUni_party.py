def create_reservations(n: int):
    reservations = set()
    for _ in range(n):
        reservations.add(input())
    return reservations

def process(reservations: set):
    guest = input()
    while guest != "END":
        if guest in reservations:
            reservations.remove(guest)
        guest = input()

def main():
    n = int(input())
    reservations = create_reservations(n)
    process(reservations)
    print(len(reservations))
    print('\n'.join(sorted(reservations)))

if __name__ == "__main__":
    main()