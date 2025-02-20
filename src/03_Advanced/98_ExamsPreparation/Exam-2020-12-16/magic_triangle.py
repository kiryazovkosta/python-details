def get_magic_triangle(size: int):
    result = []
    number = 1

    for index in range(size):
        if index == 0:
            result.append([1])
        elif index == 1:
            result.append([1, 1])
        else:
            prev = result[-1]
            current = [1]
            for i in range(len(prev) -1):
                number = prev[i] + prev[i+1]
                current.append(number)
            current.append(1)
            result.append(current)

    return result

get_magic_triangle(5)
get_magic_triangle(100)