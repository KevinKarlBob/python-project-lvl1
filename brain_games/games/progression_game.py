from random import randint
from prompt import string


def progressive_game_begin():
    rand_number1 = randint(0, 100)
    rand_number2 = randint(1, 10)
    rand_number3 = randint(0, 9)
    limit = rand_number2 * 10 + rand_number1
    progressive = [x for x in range(rand_number1, limit, rand_number2)]
    correct_answer = progressive[rand_number3]
    progressive[rand_number3] = '.'
    print(f'Question:{progressive}')
    answer = string('Your answer: ')
    if str(correct_answer) == answer:
        return True,
    else:
        return False, answer, correct_answer
