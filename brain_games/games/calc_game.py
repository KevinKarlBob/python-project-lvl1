from operator import add, sub, mul
from random import randint
from prompt import string

math_operators = ['+', '-', '*']

transfer_math_operators = {'+': add, '-': sub, '*': mul}


def calc_game_begin():
    rnd_num1 = randint(0, 100)
    rnd_num2 = randint(0, 100)
    rnd_oper = math_operators[randint(0, 2)]
    print(f'Question:{rnd_num1} {rnd_oper} {rnd_num2}')
    answer = string('Your answer: ')
    expression_answer = transfer_math_operators[rnd_oper](rnd_num1, rnd_num2)
    if str(expression_answer) == answer:
        return True,
    else:
        return False, answer, expression_answer
