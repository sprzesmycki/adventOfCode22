from collections.abc import Generator


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row[:-1]


def day_7_part_1():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")


def day_7_part_2():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")


if __name__ == '__main__':
    day_7_part_1()
    day_7_part_2()
