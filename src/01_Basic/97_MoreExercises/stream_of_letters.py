secrets = {
    "c": 0,
    "o": 0,
    "n": 0,
}

def reset():
    for secret in secrets:
        secrets[secret] = 0

def secret_found():
    for secret in secrets:
        if secrets[secret] == 0:
            return False
    return True

def main():
    word: str = ""
    while True:
        letter = input()
        if letter == "End":
            break

        if not letter.isalpha():
            continue

        if letter in secrets:
            if secrets[letter] == 0:
                secrets[letter] += 1
                if secret_found():
                    print(f"{word}", end=" ")
                    word = ""
                    reset()
            else:
                word += letter
        else:
            word += letter

if __name__ == "__main__":
    main()