from prompt import string


def greeting(game_name=None):
    print('Welcome to the Brain Games!')
    _, _, phrase = game_name()
    print(phrase)
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(data):
    if isinstance(data, tuple):
        if len(data) == 2:
            print(f'Question: {data[0]} {data[1]}')
        elif len(data) == 3:
            print(f'Question: {data[0]} {data[1]} {data[2]}')
    else:
        print(f'Question: {data}')



