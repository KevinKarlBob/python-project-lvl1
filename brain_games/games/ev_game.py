from random import randint

from prompt import string


def guess_even():
    number = randint(0, 100)
    print(f'Question:{number}')
    answer = string('Your answer: ')
    expected_answer = 'yes' if number % 2 == 0 else 'no'
    return answer, expected_answer
