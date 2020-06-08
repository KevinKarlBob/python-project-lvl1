import math
from random import randint

from prompt import string


def is_prime():
    number = randint(0, 100)
    print(f'Question:{number} ')
    answer = string('Your answer: ')
    if number % 2 == 0:
        return answer, 'no'
    upper_border_divisor = int(math.sqrt(number))
    for divisor in range(3, upper_border_divisor):
        if number % divisor == 0:
            return answer, 'no'
    return answer, 'yes'
