import io

def read_rules(filename: str):
    """
    Read rules from input file in format XX|YY
    :param filename:
    :return:
    """
    rules = {}
    with open("rules.txt", "r") as rules_file:
        for rule in rules_file.readlines():
            key, value = rule.strip().split("|")
            key = int(key)
            value = int(value)
            if key not in rules:
                rules[key] = []
            rules[key].append(int(value))
    return rules

def correct_update(index, lst, rul):
    if index >= len(lst) - 1:
        return lst

    for i in range(len(lst) - 1):
        f = lst[i]
        s = lst[i + 1]
        if s not in rul[f]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            correct_update(0, lst, rul)
    return lst

def first(rules: dict, updates_list: list[str]) -> int:
    total_sum = 0
    for update in updates_list:
        is_valid = True
        updates = [int(n) for n in update.strip().split(",")]
        length = len(updates)
        for index in range(length - 1):
            f = updates[index]
            s = updates[index + 1]
            if s not in rules[f]:
                is_valid = False
                break
        if is_valid:
            total_sum += updates[length // 2]

    return total_sum

def second(rules: dict, updates_list: list[str]):
    total_sum = 0
    for update in updates_list:
        is_valid = True
        updates = [int(n) for n in update.strip().split(",")]
        length = len(updates)

        for index in range(length - 1):
            f = updates[index]
            s = updates[index + 1]
            if s not in rules[f]:
                is_valid = False
                break

        if not is_valid:
            correct_update(0, updates, rules)
            total_sum += updates[length // 2]

    return total_sum

def main():
    rules = read_rules("rules.txt")
    with open("updates.txt", "r") as updates_file:
        updates_list = updates_file.readlines()
        first_result = first(rules, updates_list)
        print(first_result)
        second_result = second(rules, updates_list)
        print(second_result)




if __name__ == "__main__":
    main()