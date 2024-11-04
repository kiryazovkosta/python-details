deck = input().split(" ")
shuffles = int(input())

length = len(deck) // 2
for _ in range(shuffles):
    first_half = deck[:length]
    second_half = deck[length:]

    for index in range(length):
        deck[2 * index] = first_half[index]
        deck[2 * index + 1] = second_half[index]

print(deck)