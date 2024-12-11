def tribonacci_array(size: int) -> list[int]:
    if size == 1:
        return [1]
    elif size == 2:
        return [1, 1]
    else:
        numbers = [1, 1, 2]
        for index in range(3, size):
            numbers.append(numbers[index - 3] + numbers[index - 2] + numbers[index - 1])
    
        return numbers

array = tribonacci_array(int(input()))
print(" ".join(str(num) for num in array))