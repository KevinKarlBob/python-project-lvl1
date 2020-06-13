import math
from random import randint


def is_prime():
    number = randint(0, 100)
    return number, 'yes' if check_prime(number) else 'no'


def check_prime(number):
    if number % 2 == 0:
        return False
    upper_border_divisor = int(math.sqrt(number))
    for divisor in range(3, upper_border_divisor):
        if number % divisor == 0:
            return False
    return True
