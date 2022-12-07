from collections.abc import Generator


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row[:-1]


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if a_set & b_set:
        return a_set & b_set


def get_priority_of_member(common):
    i = ord(common)
    if i in range(65, 91):
        return i - 38
    elif i in range(97, 123):
        return i - 96


def count_priorities_in_one_row():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    common_members = []
    result = 0
    for row in file:
        first_compartment = row[:len(row) // 2]
        second_compartment = row[len(row) // 2:]
        s = set(first_compartment)
        b = set(second_compartment)
        common = common_member(s, b)
        priority = get_priority_of_member(common.pop())
        result += priority
        common_members.append(common)
    print(result)


def count_priorities_in_three_rows():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    result = 0
    rucksacks_group = []
    for row in file:
        if len(rucksacks_group) < 3:
            rucksacks_group.append(row)
        if len(rucksacks_group) == 3:
            common = common_member(rucksacks_group[0], rucksacks_group[1])
            common = common_member(common, rucksacks_group[2])
            priority = get_priority_of_member(common.pop())
            result += priority
            rucksacks_group.clear()
    print(result)


if __name__ == '__main__':
    count_priorities_in_one_row()
    count_priorities_in_three_rows()
