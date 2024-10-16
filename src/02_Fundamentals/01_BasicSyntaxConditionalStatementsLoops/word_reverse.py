def reverse(text: str) -> str:
    return text[::-1]

def main():
    text = input()
    print(reverse(text))

if __name__ == "__main__":
    main()