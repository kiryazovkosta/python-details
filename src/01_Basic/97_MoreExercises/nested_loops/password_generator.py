n = int(input())
l = int(input())

a = ord("a")
counter = 0
last_start = 0
for x1 in range(1, n + 1):
    for x2 in range(1, n + 1):
        last_start = x1 if x1 >= x2 else x2
        for x3 in range(a, a + l):
            for x4 in range(a, a + l):
                for x5 in range(last_start + 1, n + 1):
                    counter+=1
                    if x5 > x1 and x5 > x2:
                        print(f"{x1}{x2}{chr(x3)}{chr(x4)}{x5}", end =" ")