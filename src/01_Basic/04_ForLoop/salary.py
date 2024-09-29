import sys

tabs_length = int(input())
salary = float(input())

fines_sum = 0
for i in range(0, tabs_length):
    url = input()
    if url == "Facebook":
        salary -= 150
    elif url == "Instagram":
        salary -= 100
    elif url == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        sys.exit(0)

print(int(salary))
