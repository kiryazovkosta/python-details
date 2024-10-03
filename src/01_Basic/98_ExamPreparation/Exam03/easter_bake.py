import sys
from math import ceil

SUGAR_PACK_SIZE = 950
FLOUR_PACK_SIZE = 750

cosunaks = int(input())
total_used_sugar = 0
total_used_flour = 0
max_used_sugar = -sys.maxsize
max_used_flour = -sys.maxsize
for _ in range(cosunaks):
    used_sugar = int(input())
    used_flour = int(input())
    total_used_sugar += used_sugar
    total_used_flour += used_flour
    if used_sugar > max_used_sugar:
        max_used_sugar = used_sugar
    if used_flour > max_used_flour:
        max_used_flour = used_flour

used_sugar_packages = ceil(total_used_sugar/SUGAR_PACK_SIZE)
used_flour_packages = ceil(total_used_flour/FLOUR_PACK_SIZE)

print(f"Sugar: {used_sugar_packages}")
print(f"Flour: {used_flour_packages}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")