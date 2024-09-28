members_count = int(input())

grades_sum = 0.0
grades_count = 0
name = ""

while name != "Finish":
    name = input()
    if name == "Finish":
        break

    current_grades = 0
    for _ in range(0, members_count):
       current_grades += float(input())

    average_grade = current_grades / members_count
    print(f"{name} - {average_grade:.2f}.")
    grades_sum += average_grade
    grades_count += 1

print(f"Student's final assessment is {grades_sum/grades_count:.2f}.")
