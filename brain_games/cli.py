from prompt import string


def welcome_user():
    name = string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')
    return name
