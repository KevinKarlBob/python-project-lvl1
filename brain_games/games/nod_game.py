import math
from random import randint

from prompt import string


def nod_game_begin():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    print(f'Question:{first_number} {second_number}')
    answer = string('Your answer: ')
    expected_answer = math.gcd(first_number, second_number)
    return answer, expected_answer
