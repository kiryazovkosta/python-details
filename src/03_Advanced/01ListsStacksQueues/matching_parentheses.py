def main():
    text = input()
    brakets = []
    for index in range(len(text)):
        ch = text[index]
        if ch == "(":
            brakets.append(index)
        elif ch == ")":
            start_index = brakets.pop()
            expression = text[start_index:index+1]
            print(expression)

if __name__ == "__main__":
    main()