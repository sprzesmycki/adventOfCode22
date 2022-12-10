from collections.abc import Generator


def read_file(path: str) -> Generator:
    for row in open(path):
        yield row[:-1]


def get_points_for_choosen_sign(sign) -> int:
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    match sign:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3


def get_points_for_battle_results(player, opp):
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    if (opp == 'A' and player == 'X') or (opp == 'B' and player == 'Y') or (opp == 'C' and player == 'Z'):
        return 3
    elif (opp == 'A' and player == 'Y') or (opp == 'B' and player == 'Z') or (opp == 'C' and player == 'X'):
        return 6
    elif (opp == 'A' and player == 'Z') or (opp == 'B' and player == 'X') or (opp == 'C' and player == 'Y'):
        return 0
    else:
        print()


def get_sign_for_expected_result(exp_result, opp):
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    if (opp == 'A' and exp_result == 'Y') or (opp == 'B' and exp_result == 'X') or (opp == 'C' and exp_result == 'Z'):
        return 'X'
    elif (opp == 'A' and exp_result == 'Z') or (opp == 'B' and exp_result == 'Y') or (opp == 'C' and exp_result == 'X'):
        return 'Y'
    elif (opp == 'A' and exp_result == 'X') or (opp == 'B' and exp_result == 'Z') or (opp == 'C' and exp_result == 'Y'):
        return 'Z'
    else:
        print()


# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors


def calculate_total_score_part1():
    # file = read_file("./sample.txt")
    file = read_file("./input.txt")
    score = 0
    for row in file:
        opponent, you = row.split(" ")
        points_for_sign = get_points_for_choosen_sign(you)
        points_for_results = get_points_for_battle_results(you, opponent)
        score += points_for_results + points_for_sign
    print(score)


def calculate_total_score_part2():
    # file = read_file("./2/sample.txt")
    file = read_file("./2/input.txt")
    score = 0
    for row in file:
        opponent, result = row.split(" ")
        player_sign = get_sign_for_expected_result(result, opponent)
        points_for_sign = get_points_for_choosen_sign(player_sign)
        points_for_results = get_points_for_battle_results(player_sign, opponent)
        score += points_for_results + points_for_sign
    print(score)


if __name__ == '__main__':
    calculate_total_score_part1()
    calculate_total_score_part2()
