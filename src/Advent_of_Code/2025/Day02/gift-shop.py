import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils_functions import read_single

def first(filename: str) -> int:
    line = read_single(filename)
    ranges = [(int(p.split('-')[0]), int(p.split('-')[1])) for p in [pear for pear in line.split(',')]]
    total = 0
    for start_value, end_value in ranges:
        for id in range(start_value, end_value + 1):
            if digits_count(id) % 2 != 0:
                continue
            if number_is_invalid_id(id):
                total = total + id
    
    return total

def second(filename: str) -> int:
    line = read_single(filename)
    ranges = [(int(p.split('-')[0]), int(p.split('-')[1])) for p in [pear for pear in line.split(',')]]
    total = 0
    for start_value, end_value in ranges:
        for id in range(start_value, end_value + 1):
            if number_is_second_invalid_id(id):
                total = total + id
    
    return total

def digits_count(number: int) -> int:
    temp = number
    count = 0
    while temp >= 1:
        temp = temp / 10
        count = count + 1
    
    return count

def number_is_invalid_id(id: int) -> bool:
    id_as_string = str(id)
    middle = (len(id_as_string) // 2)
    for index in range(len(id_as_string) // 2):
        if id_as_string[index] != id_as_string[middle + index]:
            return False
    return True

def number_is_second_invalid_id(id: int) -> bool:
    id_as_string = str(id)
    elements = set(id_as_string)
    if len(elements) == 1 and id > 10:
        return True
    elif (len(id_as_string) % 2 == 0 and len(id_as_string) >= 4) \
        or len(id_as_string) == 9:
        if number_is_invalid_id(id):
            return True
        
        middle = (len(id_as_string) // 2)
        for index in range(2, middle + 1, 1):
            unique = set()
            for subIndex in range(0, len(id_as_string), index):
                unique.add(id_as_string[subIndex:subIndex+index]) 

            if len(unique) == 1:
                return True
    else:
        return False
        

def main():
    print(f"First task: {first('Day02/input.txt')}")
    print(f"Second task: {second('Day02/input.txt')}")

if __name__ == "__main__":
    main()