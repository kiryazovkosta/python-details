from xml.etree.ElementPath import prepare_parent

rules = {
    47: [53,13,61,29],
    97: [13,61,47,29,53,75],
    75: [29,53,47,61,13],
    61: [13,53,29],
    29: [13],
    53: [29,13],
    13: []
}
updates1 = [75, 97, 47, 61, 53]
updates2 = [61,13,29]
updates3 = [97,13,75,29,47]


def correct(index, length, lst):
    if index == length - 1:
        return lst

    for i in range(index, length - 1):
        f = lst[i]
        s = lst[i + 1]
        if s not in rules[f]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            correct(i + 1, length, lst)
    return lst

correct(0, len(updates1), updates1)
print(updates1)
correct(0, len(updates2), updates2)
print(updates2)
correct(0, len(updates3), updates3)
print(updates3)