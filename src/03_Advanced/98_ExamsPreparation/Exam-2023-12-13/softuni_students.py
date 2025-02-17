def softuni_students(*args, **kwargs) -> str:
    result = []

    courses = {}
    for number, name in args:
        if number not in courses:
            courses[number] = []
        courses[number].append(name)

    courses_list = {}
    for number, name in kwargs.items():
        if number in courses:
            courses_list[name] = courses[number]
            del courses[number]

    for course_name, students in courses_list.items():
        for student in sorted(students):
            result.append(f"*** A student with the username {student} has successfully finished the course {course_name}!")

    if courses:
        result.append(f"!!! Invalid course students: {', '.join(sorted([name for key, value in courses.items() for name in value]))}")



    return '\n'.join(result)

print(
    softuni_students(
        ('id_1', 'Kaloyan9905'),
        ('id_2', 'Miss1'),
        ('id_3', 'Miss2'),
        ('id_4', 'Miss3'),
        ('id_5', 'Miss4'),
        ('id_2', 'Miss5'),
        ('id_3', 'Miss6'),
        id_1='Python Web Framework',))
print("===============================================")
print(
    softuni_students(
        ('id_7', 'Silvester1'),
        ('id_32', 'Katq21'),
        ('id_7', 'The programmer'),
        id_76='Spring Fundamentals',
        id_7='Spring Advanced',))
print("===============================================")
print(
    softuni_students(
        ('id_22', 'Programmingkitten'),
        ('id_11', 'MitkoTheDark'),
        ('id_321', 'Bobosa253'),
        ('id_08', 'KrasimirAtanasov'),
        ('id_32', 'DaniBG'),
        id_321='HTML & CSS',
        id_22='Machine Learning',
        id_08='JS Advanced',))
print("===============================================")