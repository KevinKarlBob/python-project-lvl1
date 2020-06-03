from random import randint
from prompt import string


def guess_even():
    rnd_num = randint(0, 100)
    print(f'Question:{rnd_num}')
    answer = string('Your answer: ')
    if rnd_num % 2 == 0 and answer == 'yes' or \
            rnd_num % 2 != 0 and answer == 'no':
        return True,
    else:
        correct_answer = 'yes'
        if answer != 'no':
            correct_answer = 'no'
        return False, answer, correct_answer
