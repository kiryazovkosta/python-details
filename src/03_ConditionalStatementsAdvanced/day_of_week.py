number = int(input())
match number:
    case 1:
        name = "Monday"
    case 2:
        name = "Tuesday"
    case 3:
        name = "Wednesday"
    case 4:
        name = "Thursday"
    case 5:
        name = "Friday"
    case 6:
        name = "Saturday"
    case 7:
        name = "Sunday"
    case _:
        name = "Error"

print(name)