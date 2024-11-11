def messaging(sequence, text):
    numbers = sequence.split()
    message = []

    for number in numbers:
        index = sum(int(digit) for digit in number)
        index %= len(text)
        message.append(text[index])
        text = text[:index] + text[index + 1:]
    return ''.join(message)

def main():
    sequence = input("")
    text = input("")
    print(messaging(sequence, text))

if __name__ == "__main__":
    main()