repeat_string = lambda string, count: string * count

def main():
    string = input()
    count = int(input())
    print(repeat_string(string=string, count=count))

if __name__ == "__main__":
    main()