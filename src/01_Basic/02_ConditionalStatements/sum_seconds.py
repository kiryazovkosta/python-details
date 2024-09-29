a = int(input())
b = int(input())
c = int(input())

total_seconds = a + b + c
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f'{minutes}:{seconds:02d}')