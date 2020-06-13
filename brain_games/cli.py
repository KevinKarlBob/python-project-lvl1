from prompt import string
from brain_games.game_factory import game_dictionary


def greeting(game_indicator=None):
    print('Welcome to the Brain Games!')
    if game_indicator:
        print(game_dictionary[game_indicator][0])
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
