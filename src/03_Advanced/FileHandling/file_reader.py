try:
    print(sum(int(n) for n in open("files/numbers.txt", "r").readlines()))
except FileNotFoundError:
    print("File not found")
        