vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

def clear_vowels(text: str) -> str:
    return "".join([char for char in text if char not in vowels])

def main():
    text = input()
    cleared_text = clear_vowels(text)
    print(cleared_text)

if __name__ == "__main__":
    main()