from operator import add, sub, mul
from random import randint

from prompt import string

transfer_math_operators = {'+': add, '-': sub, '*': mul}


def calc_game_begin():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = list(transfer_math_operators)[randint(0, 2)]
    print(f'Question:{first_number} {operation} {second_number}')
    answer = string('Your answer: ')
    math_func = transfer_math_operators[operation]
    expected_result = math_func(first_number, second_number)
    return answer, expected_result
