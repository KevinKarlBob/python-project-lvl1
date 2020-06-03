from random import randint
from prompt import string


def nod_game_begin():
    rnd_num1 = randint(0, 100)
    rnd_num2 = randint(0, 100)
    print(f'Question:{rnd_num1} {rnd_num2}')
    answer = string('Your answer: ')
    while rnd_num1 != rnd_num2:
        if rnd_num1 > rnd_num2:
            rnd_num1 = rnd_num1 - rnd_num2
        else:
            rnd_num2 = rnd_num2 - rnd_num1
    if rnd_num1 == answer:
        return True,
    else:
        return False, answer, rnd_num1
