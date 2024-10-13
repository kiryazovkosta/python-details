begin: int = int(input())
end: int = int(input())
magic: int = int(input())

combination: int = 0
match_found: bool = False
for a in range(begin, end + 1):
    for b in range(begin, end +1):
        combination += 1
        if a + b == magic:
            print(f"Combination N:{combination} ({a} + {b} = {magic})")
            match_found = True
            break
    if match_found:
        break
else:
    print(f"{combination} combinations - neither equals {magic}")
