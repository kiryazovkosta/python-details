def calc_ascii_sum(text: str)-> int:
    return sum([ord(letter) for letter in text])

def main():
    odd, even = read_names()
    odd_sum = sum(odd)
    even_sum = sum(even)
    if odd_sum > even_sum:
        difference = odd.difference(even)
        print(', '.join(map(str, difference)))
    elif even_sum > odd_sum:
        difference = odd.symmetric_difference(even)
        print(', '.join(map(str, difference)))
    else:
        union = odd.union(even)
        print(', '.join(map(str, union)))


def read_names():
    n = int(input())
    odd = set()
    even = set()
    for index in range(1, n + 1):
        name = input()
        name_ascii_sum = int(calc_ascii_sum(name) / index)
        if name_ascii_sum % 2 == 0:
            even.add(name_ascii_sum)
        else:
            odd.add(name_ascii_sum)
    return odd, even


if __name__ == "__main__":
    main()