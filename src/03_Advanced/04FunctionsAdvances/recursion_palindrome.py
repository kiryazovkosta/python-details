def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)

print(palindrome("abcdcba", 0))
print(palindrome("peter", 0))