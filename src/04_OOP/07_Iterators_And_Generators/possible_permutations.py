from itertools import permutations

def possible_permutations(ls):
    perms = permutations(ls)
    for p in perms:
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]
print("#########################################")
[print(n) for n in possible_permutations([1])]