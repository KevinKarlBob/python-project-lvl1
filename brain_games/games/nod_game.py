from random import randint
from prompt import string


def nod_game_begin():
    rand_number1 = randint(0, 100)
    rand_number2 = randint(0, 100)
    print(f'Question:{rand_number1} {rand_number2}')
    answer = string('Your answer: ')
    while rand_number1 != rand_number2:
        if rand_number1 > rand_number2:
            rand_number1 = rand_number1 - rand_number2
        else:
            rand_number2 = rand_number2 - rand_number1
    if rand_number1 == answer:
        return True,
    else:
        return False, answer, rand_number1
