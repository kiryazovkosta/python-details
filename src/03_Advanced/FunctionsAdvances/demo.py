import requests

# def sum_nums(a: int, b: int = 10, *args) -> int:
#     result = a + b
#     for el in args:
#         result += el
#
#     return result
#
# def sum_nums_2(*args) -> int:
#     result = 0
#     for el in args:
#         result += el
#
#     return result
#
# print(sum_nums(2, 5))
# print(sum_nums(5))
# print(sum_nums(4, 6, 1, 2, 4, 5))
#
# print(sum_nums_2("1", "2", "3"))
from keyword import kwlist


# def greetings(name, **kwargs) -> str:
#     result = f"Hello {name}!"
#     for key, value in kwargs.items():
#         result += "\n"
#         result += f"{key} -> {value}"
#     return result
#
#
# print(greetings("Test", city="Sofia", country="Bulgaria"))


# a = [100, 1, -1, 5]
# result = sorted(a)
# print(a)
# print(result)


# data = { 'Peter': 21, 'George': 18, 'John': 45, 'Atanas': 25, 'Kosta': 33, 'Ivelin': 31, 'Vladimir': 21, 'Maria': 30, 'Petar': 10 }
# result = sorted(data.items(), key=lambda kvp: -kvp[1])
# print(result)
# result = sorted(data.items(), key=lambda kvp: kvp[0], reverse=True)
# print(result)

response = requests.get('https://judge.softuni.org/Contests/Compete/Index/1839#7')
print(response.status_code)
print(*response)