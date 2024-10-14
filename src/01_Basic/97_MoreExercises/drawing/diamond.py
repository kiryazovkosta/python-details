def print_diamond(n):

    for i in range((n + 1) // 2):
        left_right = (n - 1) // 2 - i
        mid = n - 2 * left_right - 2

        if mid >= 0:
            print('-' * left_right + '*' + '-' * mid + '*' + '-' * left_right)
        else:
            print('-' * left_right + '*' + '-' * left_right)

    for i in range((n - 1) // 2 - 1, -1, -1):
        left_right = (n - 1) // 2 - i
        mid = n - 2 * left_right - 2

        if mid >= 0:
            print('-' * left_right + '*' + '-' * mid + '*' + '-' * left_right)
        else:
            print('-' * left_right + '*' + '-' * left_right)

def main():
    n = int(input())
    print_diamond(n)

if __name__ == "__main__":
    main()