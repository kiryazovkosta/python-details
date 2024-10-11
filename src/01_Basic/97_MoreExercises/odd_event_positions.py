import sys
numbers = int(input())

OddSum=0 
OddMin=sys.maxsize
OddMax=-sys.maxsize
EvenSum=0
EvenMin=sys.maxsize
EvenMax=-sys.maxsize
for index in range(1, numbers + 1):
    number = float(input())
    if index % 2 != 0:
        OddSum += number
        if OddMin > number:
            OddMin = number
        if OddMax < number:
            OddMax = number
    else:
        EvenSum += number
        if EvenMin > number:
            EvenMin = number
        if EvenMax < number:
            EvenMax = number

print(f"OddSum={OddSum:.2f},") 
print(f"OddMin={OddMin:.2f}," if OddMin != sys.maxsize else "OddMin=No,") 
print(f"OddMax={OddMax:.2f}," if OddMax != -sys.maxsize else "OddMax=No,")
print(f"EvenSum={EvenSum:.2f},") 
print(f"EvenMin={EvenMin:.2f}," if EvenMin != sys.maxsize else "EvenMin=No,")
print(f"EvenMax={EvenMax:.2f}" if EvenMax != -sys.maxsize else "EvenMax=No")