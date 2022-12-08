from collections.abc import Generator


def read_file(path: str):
    for row in open(path):
        return row[:-1]


def search_for_marker(file, marker_length):
    for i in range(len(list(file))):
        marker = file[i:i + marker_length]
        if len(marker) == len(set(marker)):
            print(i+marker_length)
            break


def day_6_part_1():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    search_for_marker(file, 4)


def day_6_part_2():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    search_for_marker(file, 14)


if __name__ == '__main__':
    day_6_part_1()
    day_6_part_2()
