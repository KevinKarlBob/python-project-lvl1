from random import randint

from prompt import string


def nod_game_begin():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    print(f'Question:{first_number} {second_number}')
    answer = string('Your answer: ')
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return answer, first_number
