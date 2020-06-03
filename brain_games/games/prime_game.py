import math
from operator import add, sub, mul
from random import randint
from prompt import string

math_operators = ['+', '-', '*']

transfer_math_operators = {'+': add, '-': sub, '*': mul}


def is_prime():
    rand_number1 = randint(0, 100)
    print(f'Question:{rand_number1} ')
    answer = string('Your answer: ')
    correct_answer = 'yes'
    if rand_number1 % 2 == 0:
        correct_answer = 'no'
        if answer == 'yes':
            return False, answer, correct_answer
        else:
            return True,
    delimiter = 3
    limit = int(math.sqrt(rand_number1))
    while delimiter <= limit:
        if rand_number1 % delimiter == 0:
            correct_answer = 'no'
            break
        delimiter += 2
    if answer == correct_answer:
        return True,
    else:
        return False, answer, correct_answer
