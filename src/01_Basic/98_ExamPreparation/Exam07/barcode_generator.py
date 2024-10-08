begin = int(input())
end = int(input())

begin_first = begin // 1000
begin_second = (begin // 100) % 10
begin_third = (begin // 10) % 10
begin_fourth = begin % 10

end_first = end // 1000
end_second = (end // 100) % 10
end_third = (end // 10) % 10
end_fourth = end % 10

for a in range(begin[0], end_first + 1):
    for b in range(begin_second, end_second + 1):
        for c in range(begin_third, end_third + 1):
            for d in range(begin_fourth, end_fourth + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end= " ")