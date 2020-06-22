import math
from random import randint


def prime_game_begin():
    phrase = 'Answer "yes" if given number is prime. Otherwise answer "no"'
    number = randint(0, 100)
    expected_answer = 'yes' if is_prime(number) else 'no'
    return number, expected_answer, phrase


def is_prime(number):
    if number % 2 == 0:
        return False
    upper_border_divisor = int(math.sqrt(number))
    for divisor in range(3, upper_border_divisor):
        if number % divisor == 0:
            return False
    return True
