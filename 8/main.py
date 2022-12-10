from collections.abc import Generator

trees = []


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row[:-1]


def get_trees_in_direction(row, column, direction):
    temp_trees = []
    row_move = 0
    column_move = 0
    match direction:
        case "top":
            row_move = -1
        case "bottom":
            row_move = 1
        case "left":
            column_move = -1
        case "right":
            column_move = 1

    if row_move == -1:
        for i in range(0, row):
            tree = trees[i][column]
            temp_trees.append(tree)
    if row_move == 1:
        for i in range(row + 1, len(trees)):
            tree = trees[i][column]
            temp_trees.append(tree)

    if column_move == -1:
        for i in range(0, column):
            tree = trees[row][i]
            temp_trees.append(tree)
    if column_move == 1:
        for i in range(column + 1, len(trees[row])):
            tree = trees[row][i]
            temp_trees.append(tree)

    return temp_trees


def is_tree_visible(tree_height, trees_line):
    return any(int(i) >= tree_height for i in trees_line)


def check_if_tree_is_awesome_enough_to_build_tree_house(tree_height, row, column):
    row_length = len(trees[row])
    column_length = len(trees[column])
    if row in [row_length - 1, 0] or column in [column_length - 1, 0]:
        return False

    top_trees = get_trees_in_direction(row, column, direction="top")
    bottom_trees = get_trees_in_direction(row, column, direction="bottom")
    left_trees = get_trees_in_direction(row, column, direction="left")
    right_trees = get_trees_in_direction(row, column, direction="right")

    left_side = is_tree_visible(tree_height, left_trees)
    right_side = is_tree_visible(tree_height, right_trees)
    top_side = is_tree_visible(tree_height, top_trees)
    bottom_side = is_tree_visible(tree_height, bottom_trees)

    return left_side and right_side and top_side and bottom_side


def get_trees(file):
    for row in file:
        trees_in_row = []
        for tree in row:
            trees_in_row.append(int(tree))
        trees.append(trees_in_row.copy())


def day_8_part_1():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    get_trees(file)

    awesome_trees_counter = 0
    useless_trees_counter = 0

    for row, tree_row in enumerate(trees):
        for column, tree in enumerate(tree_row):
            is_tree_awesome = check_if_tree_is_awesome_enough_to_build_tree_house(tree, row, column)
            if is_tree_awesome:
                print(row, column, tree)
                awesome_trees_counter += 1
            else:
                useless_trees_counter += 1
    print("Awe: ", awesome_trees_counter)
    print("Use: ", useless_trees_counter)


def get_score_in_direction(trees_list, tree_height):
    score = 0
    for tree in trees_list:
        if tree < tree_height:
            score += 1
        else:
            score += 1
            break

    return score


def count_scenic_score_for_tree(tree_height, row, column):
    row_length = len(trees[row])
    column_length = len(trees[column])
    if row in [row_length - 1, 0] or column in [column_length - 1, 0]:
        return 0

    top_trees = get_trees_in_direction(row, column, direction="top")
    top_trees.reverse()
    top_score = get_score_in_direction(top_trees, tree_height)

    bottom_trees = get_trees_in_direction(row, column, direction="bottom")
    bottom_score = get_score_in_direction(bottom_trees, tree_height)

    left_trees = get_trees_in_direction(row, column, direction="left")
    left_trees.reverse()
    left_score = get_score_in_direction(left_trees, tree_height)

    right_trees = get_trees_in_direction(row, column, direction="right")
    right_score = get_score_in_direction(right_trees, tree_height)
    return top_score * bottom_score * left_score * right_score


def day_8_part_2():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    get_trees(file)

    scenic_score = 0
    for row, tree_row in enumerate(trees):
        for column, tree in enumerate(tree_row):
            tree_score = count_scenic_score_for_tree(tree, row, column)
            if tree_score > scenic_score:
                scenic_score = tree_score
    print("Scenic score: ", scenic_score)


if __name__ == '__main__':
    # day_8_part_1()
    day_8_part_2()
