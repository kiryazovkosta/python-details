allowed_failed_exams = int(input())

grades_sum = 0.0
last_exam_name = ""
failed_exams = 0
is_success = True
grades_counter = 0

while True:
    name = input()
    if name == "Enough":
        break

    grades_counter += 1
    grade = int(input())
    if grade <= 4:
        failed_exams += 1
        grades_sum += grade
        if failed_exams == allowed_failed_exams:
            is_success = False
            break
    else:
        grades_sum += grade
        last_exam_name = name

if is_success:
    print(f"Average score: {grades_sum/grades_counter:.2f}")
    print(f"Number of problems: {grades_counter}")
    print(f"Last problem: {last_exam_name}")
else:
    print(f"You need a break, {failed_exams} poor grades.")