NON_PURESR_SYMBOLS = [",", ".", "_"]

def is_pure(string: str):
    for ch in string:
        if ch in NON_PURESR_SYMBOLS:
            return False
    return True

def main():
    size = int(input())
    for _ in range(size):
        text = input()
        print(f"{text} is pure.") if is_pure(text) else print(f"{text} is not pure!") 

if __name__ == "__main__":
    main()