from random import randint
from prompt import string


def progressive_game_begin():
    rnd_num1 = randint(0, 100)
    rnd_num2 = randint(1, 10)
    rnd_num3 = randint(0, 9)
    limit = rnd_num2 * 10 + rnd_num1
    progressive = [x for x in range(rnd_num1, limit, rnd_num2)]
    correct_answer = progressive[rnd_num3]
    progressive[rnd_num3] = '.'
    print(f'Question:{progressive}')
    answer = string('Your answer: ')
    if str(correct_answer) == answer:
        return True,
    else:
        return False, answer, correct_answer
