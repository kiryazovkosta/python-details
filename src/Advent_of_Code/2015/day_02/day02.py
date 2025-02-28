def first():
    with open("input_01.txt") as file:
        total_sum = 0
        for line in file.readlines():
            l, w, h = list(map(int,  line.split('x')))
            total_sum += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

    return total_sum

def second():
    with open("input_01.txt") as file:
        total_sum = 0
        for line in file.readlines():
            s = sorted(map(int, line.split('x')))
            total_sum += (s[0]+s[0]+s[1]+s[1]) + (s[0]*s[1]*s[2])

    return total_sum


if __name__ == "__main__":
    print(first())
    print(second())