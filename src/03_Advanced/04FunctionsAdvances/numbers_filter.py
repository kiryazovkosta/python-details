def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == "even":
            result["even"] = [n for n in value if n % 2 == 0]
        if key == "odd":
            result["odd"] = [n for n in value if n % 2 != 0]

    result = {k: v for k, v in sorted(result.items(), key=lambda kvp: -len(kvp[1]))}
    return result

print(
    even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    )
)

print(
    even_odd_filter(
        odd=[2, 2, 30, 44, 10, 5],
    )
)