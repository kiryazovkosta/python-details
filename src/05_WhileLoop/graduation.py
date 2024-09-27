MAX_GRAD = 12
PASSING_GRADE = 4.00

name = input()
failed_once = False
grade_level = 1
grades_sum = 0.0

while grade_level  <= MAX_GRAD:
    year_grade = float(input())

    if year_grade >= PASSING_GRADE:
        grades_sum += year_grade
        grade_level += 1
        failed_once  = False
    elif not failed_once :
        failed_once  = True
    else:
        break

if grade_level < MAX_GRAD:
    print(f"{name} has been excluded at {grade_level} grade")
else:
    print(f"{name} graduated. Average grade: {grades_sum/MAX_GRAD:.2f}")