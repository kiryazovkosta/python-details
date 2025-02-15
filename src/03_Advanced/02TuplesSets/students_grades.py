def avg(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def main() -> None:
    n = int(input())

    students = {}
    for _ in range(n):
        name, grade = tuple(input().split())
        grade = float(grade)
        if name not in students:
            students[name] = []
        students[name].append(grade)

    for name, grades in students.items():
        grades_list = [str(f"{gr:.2f}") for gr in grades]
        print(f"{name} -> {' '.join(grades_list)} (avg: {avg(grades):.2f})")

if __name__ == "__main__":
    main()