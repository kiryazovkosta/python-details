def reverse_string(text: str) -> str:
    l = list(text)
    result = []
    while len(l) > 0:
        result.append(l.pop())
    
    return "".join(result)

def main():
    text = input()
    reversed =reverse_string(text)
    print(reversed)
    
if __name__ == "__main__":
    main()