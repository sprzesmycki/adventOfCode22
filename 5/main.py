from collections.abc import Generator

# [F]         [L]     [M]
# [T]     [H] [V] [G] [V]
# [N]     [T] [D] [R] [N]     [D]
# [Z]     [B] [C] [P] [B] [R] [Z]
# [M]     [J] [N] [M] [F] [M] [V] [H]
# [G] [J] [L] [J] [S] [C] [G] [M] [F]
# [H] [W] [V] [P] [W] [H] [H] [N] [N]
# [J] [V] [G] [B] [F] [G] [D] [H] [G]
#  1   2   3   4   5   6   7   8   9
stacks = [[],  # empty index to not confuse myself
          ['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],  # 1
          ['V', 'W', 'J'],  # 2
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],  # 3
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],  # 4
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],  # 5
          ['G', 'H', 'C', 'F', 'B', 'N', 'V', 'M'],  # 6
          ['D', 'H', 'G', 'M', 'R'],  # 7
          ['H', 'N', 'M', 'V', 'Z', 'D'],  # 8
          ['G', 'N', 'F', 'H']  # 9
          ]

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
# stacks = [[],
#           ['Z', 'N'],
#           ['M', 'C', 'D'],
#           ['P']
#           ]


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row[:-1]


def move_crates(crates_count, source_pile, target_pile):
    for x in range(0, crates_count):
        crate_to_move = stacks[source_pile].pop()
        stacks[target_pile].append(crate_to_move)


def move_crates_as_stacks(crates_count, source_pile, target_pile):
    temp_stack = []
    for x in range(0, crates_count):
        crate_to_move = stacks[source_pile].pop()
        temp_stack.append(crate_to_move)

    for stack in range(0, len(temp_stack)):
        stacks[target_pile].append(temp_stack.pop())


def get_top_crates():
    result = []
    for stack in stacks:
        if stack:  # if empty_list will evaluate as false.
            result.append(stack.pop())
    print(''.join(result))


def day_5_part_1():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    for row in file:
        row_split = row.split(' ')
        crates_count = int(row_split[1])
        source_pile = int(row_split[3])
        target_pile = int(row_split[5])
        move_crates(crates_count, source_pile, target_pile)
    get_top_crates()


def day_5_part_2():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    for row in file:
        row_split = row.split(' ')
        crates_count = int(row_split[1])
        source_pile = int(row_split[3])
        target_pile = int(row_split[5])
        move_crates_as_stacks(crates_count, source_pile, target_pile)
    get_top_crates()


if __name__ == '__main__':
    # day_5_part_1()
    day_5_part_2()
