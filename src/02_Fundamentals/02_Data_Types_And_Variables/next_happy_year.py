def is_dictinct(year):
    # year_str = str(year)
    # for x in range(0, len(year_str)):
    #     for y in range(x + 1, len(year_str)):
    #         if year_str[x] == year_str[y]:
    #             return False
    # return True
    year_str = str(year)
    return len(set(year_str)) == len(year_str)

def next_distinct_digits_year(year):
    while True:
        year += 1
        if is_dictinct(year):
            return year

def main():
    year = int(input())
    next_year = next_distinct_digits_year(year)
    print(next_year)

main()