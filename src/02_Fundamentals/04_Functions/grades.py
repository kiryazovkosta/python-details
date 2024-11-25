def print_grade(grade: float) -> str:
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 3.00 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return  "Excellent"
    else:
        raise OverflowError("Grade is out of range")

def main():
    grade = float(input())
    grade_as_text = print_grade(grade)
    print(grade_as_text)

if __name__ == "__main__":
    main()
