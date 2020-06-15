from operator import add, sub, mul
from random import randint

TRANSFER_MATH_OPERATORS = {'+': add, '-': sub, '*': mul}


def calc_game_begin():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = list(TRANSFER_MATH_OPERATORS)[randint(0, 2)]
    data = first_number, operation, second_number
    math_func = TRANSFER_MATH_OPERATORS[operation]
    expected_result = str(math_func(first_number, second_number))
    return data, expected_result
