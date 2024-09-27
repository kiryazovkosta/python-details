MAX_GRAD = 12
name = input()
already_untaken = False
grad = 1
grades_sum = 0.0
year_grade = float(input())
while grad <= MAX_GRAD:

    if year_grade >= 4.00:
        already_untaken = False
        grades_sum += year_grade
        grad += 1
    else:
        if not already_untaken:
            already_untaken = True
        else:
            break
    if grad <= MAX_GRAD:
        year_grade = float(input())

if grad < MAX_GRAD:
    print(f"{name} has been excluded at {grad} grade")
else:
    print(f"{name} graduated. Average grade: {grades_sum/MAX_GRAD:.2f}")