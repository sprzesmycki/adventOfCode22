from collections.abc import Generator


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row[:-1]


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    return a_set & b_set


def check_if_elv_is_useless(elv1, elv2):
    elv1_range = elv1.split("-")
    elv2_range = elv2.split("-")
    is_elv1_useless = int(elv1_range[0]) >= int(elv2_range[0]) and int(elv1_range[1]) <= int(elv2_range[1])
    is_elv2_useless = int(elv1_range[0]) <= int(elv2_range[0]) and int(elv1_range[1]) >= int(elv2_range[1])
    return is_elv1_useless or is_elv2_useless


def check_if_elv_is_partially_useless(elv1, elv2):
    elv1_range = elv1.split("-")
    elv2_range = elv2.split("-")
    elv1_sections = list(range(int(elv1_range[0]), int(elv1_range[1])+1))
    elv2_sections = list(range(int(elv2_range[0]), int(elv2_range[1])+1))
    return common_member(elv1_sections, elv2_sections)


def count_redundant_elves():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    result = 0
    for row in file:
        elv1, elv2 = row.split(',')
        useless = check_if_elv_is_useless(elv1, elv2)
        if useless:
            result += 1
    print(result)


def count_semi_useful_elves():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    result = 0
    for row in file:
        elv1, elv2 = row.split(',')
        useless = check_if_elv_is_partially_useless(elv1, elv2)
        if useless:
            result += 1
    print(result)


if __name__ == '__main__':
    count_redundant_elves()
    count_semi_useful_elves()
