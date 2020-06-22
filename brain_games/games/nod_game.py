import math
from random import randint


def nod_game_begin():
    phrase = 'Find the greatest common divisor of given numbers.'
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    data = first_number, second_number
    expected_answer = math.gcd(first_number, second_number)
    return data, expected_answer, phrase
