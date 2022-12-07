from collections.abc import Generator


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row


def calculate_calories():
    elves_with_list_of_calories = []
    elves_with_sum_of_calories = []
    # result = read_file("./sample.txt")
    result = read_file("./input.txt")
    calories = []
    for row in result:
        try:
            calories.append(int(row))
        except ValueError:
            elves_with_list_of_calories.append(calories.copy())
            calories.clear()
    for elv in elves_with_list_of_calories:
        elves_with_sum_of_calories.append(sum(elv))
    elves_with_sum_of_calories.sort(reverse=True)
    print(elves_with_sum_of_calories[0])
    print(sum(elves_with_sum_of_calories[0:3]))


if __name__ == '__main__':
    calculate_calories()
