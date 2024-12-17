def is_palindrome(text: str) -> bool:
    length = len(text)
    for index in range(0, length // 2):
        if text[index] != text[length - 1 - index]:
            return False
    return True

def palindrome_count(palindromes, palindrome):
    return palindromes.count(palindrome)


def main():
    words = [word for word in input().split(" ")]
    palindrome = input()
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word) 

    print(palindromes)
    print(f"Found palindrome {palindrome_count(palindromes, palindrome)} times")

if __name__ == "__main__":
    main()