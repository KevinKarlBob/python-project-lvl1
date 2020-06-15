from prompt import string

PHRASE_DICTIONARY = {
    "calc_game": "What is the result of the expression?",
    'even_game': 'Answer "yes" if number even otherwise answer "no"',
    'gcd_game': 'Find the greatest common divisor of given numbers.',
    'prm_game': 'Answer "yes" if given number is prime. Otherwise answer "no"',
    'progression_game': 'What number is missing in the progression?'
}


def greeting(game_indicator=None):
    print('Welcome to the Brain Games!')
    if game_indicator:
        print(PHRASE_DICTIONARY[game_indicator])
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
    return string("Your answer: ")
