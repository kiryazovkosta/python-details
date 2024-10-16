def main():
    budget: float = float(input())
    while True:
        command = input()
        if command == "End":
            print("You bought everything needed.")
            break
        budget -= float(command)
        if budget < 0:
            print("You went in overdraft!")
            break

if __name__ == "__main__":
    main()