from random import randint
from prompt import string


def guess_even():
    number = randint(0, 100)
    print(f'Question:{number}')
    answer = string('Your answer: ')
    if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
        return True,
    else:
        correct_answer = 'yes'
        if answer != 'no':
            correct_answer = 'no'
        return False, answer, correct_answer
