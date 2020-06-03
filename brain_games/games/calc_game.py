from operator import add, sub, mul
from random import randint
from prompt import string

math_operators = ['+', '-', '*']

transfer_math_operators = {'+': add, '-': sub, '*': mul}


def calc_game_begin():
    rand_number1 = randint(0, 100)
    rand_number2 = randint(0, 100)
    rand_operator = math_operators[randint(0, 2)]
    print(f'Question:{rand_number1} {rand_operator} {rand_number2}')
    answer = string('Your answer: ')
    expression_answer = transfer_math_operators[rand_operator](rand_number1, rand_number2)
    if str(expression_answer) == answer:
        return True,
    else:
        return False, answer, expression_answer
