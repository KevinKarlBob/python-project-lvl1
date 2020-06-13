from random import randint


def guess_even():
    number = randint(0, 100)
    expected_answer = 'yes' if number % 2 == 0 else 'no'
    return number, expected_answer
