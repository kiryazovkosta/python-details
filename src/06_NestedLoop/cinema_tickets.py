total_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0
total_student_tickets = 0

while True:
    name = input()
    if name == "Finish":
        break

    free_places = int(input())
    standard_tickets = 0
    kid_tickets = 0
    student_tickets = 0
    total_movie_tickets = 0

    while total_movie_tickets < free_places:
        ticket = input()
        if ticket == "End":
            break

        if ticket == "standard":
            standard_tickets += 1
            total_standard_tickets += 1
        elif ticket == "kid":
            kid_tickets += 1
            total_kid_tickets += 1
        else:
            student_tickets += 1
            total_student_tickets += 1
        total_movie_tickets += 1

    print(f"{name} - {total_movie_tickets / free_places * 100:.2f}% full.")
    total_tickets += total_movie_tickets

print(f"Total tickets: {total_tickets}")
print(f"{total_student_tickets/total_tickets * 100:.2f}% student tickets.")
print(f"{total_standard_tickets/total_tickets * 100:.2f}% standard tickets.")
print(f"{total_kid_tickets/total_tickets * 100:.2f}% kids tickets.")



