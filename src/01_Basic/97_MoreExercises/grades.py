students = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for _ in range(students):
    score = float(input())
    if score >= 5.00:
        p1 += 1
    elif 4.00 <= score <= 4.99:
        p2 += 1
    elif 3.00 <= score <= 3.99:
        p3 += 1
    else:
        p4 += 1
    
    p5 += score

print(f"Top students: {p1/students*100:.2f}%")
print(f"Between 4.00 and 4.99: {p2/students*100:.2f}%")
print(f"Between 3.00 and 3.99: {p3/students*100:.2f}%")
print(f"Fail: {p4/students*100:.2f}%")
print(f"Average: {p5/students:.2f}")