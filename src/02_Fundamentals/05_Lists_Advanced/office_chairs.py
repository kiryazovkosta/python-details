def check_capacity(chairs: int, peoples: int):
    capacity = chairs - peoples
    return capacity

def main():
    no_errors = True
    free_capacity = 0
    count = int(input())
    for index in range(count):
        (c, p) = [word for word in input().split(" ")]
        capacity = check_capacity(len(c), int(p))
        if capacity >= 0:
            free_capacity += capacity
        else:
            no_errors = False
            print(f"{abs(capacity)} more chairs needed in room {index+1}")

    if no_errors:
        print(f"Game On, {free_capacity} free chairs left")

if __name__ == "__main__":
    main()