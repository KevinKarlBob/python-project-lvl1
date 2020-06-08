from random import randint

from prompt import string


def progression_game_begin():
    number_for_progression = randint(0, 100)
    progression_step = randint(1, 10)
    position_to_hide = randint(0, 9)
    limit = progression_step * 10 + number_for_progression
    progression = [number for number in
                   range(number_for_progression, limit, progression_step)]
    correct_answer = progression[position_to_hide]
    progression[position_to_hide] = '.'
    print(f'Question:{progression}')
    answer = string('Your answer: ')
    return answer, correct_answer
