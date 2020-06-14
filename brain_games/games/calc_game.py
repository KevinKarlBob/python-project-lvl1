from random import randint
from brain_games.constants import transfer_math_operators


def calc_game_begin():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = list(transfer_math_operators)[randint(0, 2)]
    data = first_number, operation, second_number
    math_func = transfer_math_operators[operation]
    expected_result = str(math_func(first_number, second_number))
    return data, expected_result
