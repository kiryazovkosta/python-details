stack = []

lines = int(input())
for _ in range(lines):
    line = input()
    if line == "(":
        stack.append("(")
    elif line == ")":
        stack.pop()
    print(len(stack))
    
print(len(stack))