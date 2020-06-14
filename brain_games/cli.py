from prompt import string
from brain_games.constants import phrase_dictionary


def greeting(game_indicator=None):
    print('Welcome to the Brain Games!')
    if game_indicator:
        print(phrase_dictionary[game_indicator])
    return welcome_user()


def welcome_user():
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(data, game_indicator):
    if game_indicator == "calc_game":
        print(f'Question: {data[0]} {data[1]} {data[2]}')
    elif game_indicator == "nod_game":
        print(f'Question: {data[0]} {data[1]}')
    else:
        print(data)


def get_answer():
    answer = string("Your answer: ")
    return answer
