grades = float(input())
if 26.00 <= grades <= 35.00:
    print("Hot")
elif 20.1 <= grades <= 25.9:
    print("Warm")
elif 15.00 <= grades <= 20.00:
    print("Mild")
elif 12.00 <= grades <= 14.9:
    print("Cool")
elif 5.00 <= grades <= 11.9:
    print("Cold")
else:
    print("unknown")