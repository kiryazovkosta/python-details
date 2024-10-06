import sys
from math import floor

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

def get_word_power(word):
    power = 0
    for letter in word:
        power += ord(letter)
    return power

def is_vowel(letter):
    letter = letter.lower()
    if letter in VOWELS:
        return True
    return False

def main():
    max_power = -sys.maxsize
    max_word = ""

    word = ""
    while True:
        word = input()
        if word == "End of words":
            break
        word_power = get_word_power(word)
        if is_vowel(word[0]):
            word_power *= len(word)
        else:
            word_power = floor(word_power / 2)

        if word_power > max_power:
            max_power = word_power
            max_word = word

    print(f"The most powerful word is {max_word} - {max_power}")

if __name__ == "__main__":
    main()