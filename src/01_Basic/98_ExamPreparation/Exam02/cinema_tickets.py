total_standard_tickets = 0
total_kid_tickets = 0
total_student_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    free_seats = int(input())
    standard_tickets = 0
    kid_tickets = 0
    student_tickets = 0

    for _ in range(0, free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break

        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        else:
            student_tickets += 1

    total_standard_tickets += standard_tickets
    total_kid_tickets += kid_tickets
    total_student_tickets += student_tickets
    movie_tickets = standard_tickets + kid_tickets + student_tickets
    print(f"{movie_name} - {movie_tickets/free_seats * 100:.2f}% full.")

total_tickets = total_standard_tickets + total_kid_tickets + total_student_tickets
print(f"Total tickets: {total_tickets}")
print(f"{total_student_tickets/total_tickets * 100:.2f}% student tickets.")
print(f"{total_standard_tickets/total_tickets * 100:.2f}% standard tickets.")
print(f"{total_kid_tickets/total_tickets * 100:.2f}% kids tickets.")