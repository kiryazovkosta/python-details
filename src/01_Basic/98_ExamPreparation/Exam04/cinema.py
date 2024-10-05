capacity = int(input())
peoples_counter = 0
income = 0
while True:
    peoples = input()
    if peoples == "Movie time!":
        print(f"There are {capacity-peoples_counter} seats left in the cinema.")
        break

    peoples = int(peoples)
    peoples_counter += peoples

    if peoples_counter > capacity:
        print(f"The cinema is full.")
        peoples_counter = capacity
        break

    income += peoples * 5
    if peoples % 3 == 0:
        income -= 5

print(f"Cinema income - {income} lv.")