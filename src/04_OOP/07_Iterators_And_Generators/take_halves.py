import sys

def solution():
    def integers():
        for i in range(1, sys.maxsize):
            yield i

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for i in range(n)]

    return (take, halves, integers)

print("\n######################")
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print("\n######################")
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))