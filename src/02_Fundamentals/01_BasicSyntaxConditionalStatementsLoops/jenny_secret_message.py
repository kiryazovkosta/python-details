def greetings(name: str) -> None:
    if name == "Johnny":
        print("Hello, my love!")
    else:
        print(f"Hello, {name}!")

def main():
    name = input()
    greetings(name)

if __name__ == "__main__":
    main()