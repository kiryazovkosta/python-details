import os

def calculate_checksum(numbers: list[str]):
    checksum = 0
    for i in range(len(numbers)):
        if numbers[i] == '.':
            continue
        current = int(numbers[i]) * i
        checksum += current
    return  checksum

def create_disk(line: str) -> list[str]:
    symbols = []
    index = 0
    for idx in range(len(line)):
        if idx % 2 == 0:
            symbols.extend([str(index)]*int(line[idx]))
            index += 1
        else:
            symbols.extend(['.']*int(line[idx]))

    return symbols


def swap_slices(arr, first_index, second_index, length):
    # Extract slices
    first_part = arr[first_index:first_index + length]
    second_part = arr[second_index:second_index + length]

    arr[first_index:first_index + length] = second_part
    arr[second_index:second_index + length] = first_part

    return arr

def first(line: str) -> int:
    symbols = create_disk(line)

    start_index = 0
    end_index = len(symbols) - 1
    while end_index > start_index:
        if symbols[start_index] != '.':
            start_index += 1
        elif symbols[end_index] == '.':
            end_index -= 1
        else:
            symbols[end_index], symbols[start_index] = symbols[start_index], symbols[end_index]
            end_index -= 1
            start_index += 1

    return calculate_checksum(symbols)

def second(line: str) -> int:
    symbols = create_disk(line)
    print(''.join(symbols))
    files = [int(c) for c in line[::2]]
    frees = [int(c) for c in line[1::2]]
    if len(files) > len(frees):
        frees.append(0)

    file_step = len(files) - 1
    while file_step > 0 :
        file_index = 1 + 2 * file_step
        file_offset = sum(int(line[idx]) for idx in range(len(line)) if idx < file_index - 1)
        current_files = symbols[file_offset:file_offset + (files[file_step] * len(str(file_step)))]
        free_step = 0
        while free_step < len(frees):
            free_index = 1 + 2 * free_step
            free_offset = sum(int(line[idx]) for idx in range(len(line)) if idx < free_index)
            current_free = symbols[free_offset:free_offset + frees[free_step]]
            if len(current_free) >= len(current_files):
                print(''.join(list(map(str, current_free))))
                print(''.join(list(map(str, current_files))))
                frees[free_step] -= len(current_files)
                swap_slices(symbols, free_offset, file_offset, len(current_files))
                print(''.join(symbols))
                break
            free_step += 1
        file_step -= 1

    return calculate_checksum(symbols)

def main():
    file_path = os.path.join(os.getcwd(), "example01.txt")
    with open(file_path, "r") as input_values_file:
        file_line: str = input_values_file.readline()
        first_result = first(file_line)
        print(first_result)

        second_result = second(file_line)
        #print(second_result)
        # 00992111777.44.333....5555.6666.....8888..
        # 00992111777.44.333....5555.6666.....8888..

if __name__ == "__main__":
    main()