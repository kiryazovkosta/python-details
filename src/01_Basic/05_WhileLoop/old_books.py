searched_book = input()
counter = 0
book = input()
while book != "No More Books":
    if book == searched_book:
        print(f"You checked {counter} books and found it.")
        break
    else:
        counter += 1

    book = input()
else:
    print(f"The book you search is not here!\nYou checked {counter} books.")