import math
from random import randint
from prompt import string


def is_prime():
    rnd_num1 = randint(0, 100)
    print(f'Question:{rnd_num1} ')
    answer = string('Your answer: ')
    correct_answer = 'yes'
    if rnd_num1 % 2 == 0:
        correct_answer = 'no'
        if answer == 'yes':
            return False, answer, correct_answer
        else:
            return True,
    delimiter = 3
    limit = int(math.sqrt(rnd_num1))
    while delimiter <= limit:
        if rnd_num1 % delimiter == 0:
            correct_answer = 'no'
            break
        delimiter += 1
    if answer == correct_answer:
        return True,
    else:
        return False, answer, correct_answer
