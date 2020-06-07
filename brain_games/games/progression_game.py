from random import randint
from prompt import string


def progression_game_begin():
    number_for_progression = randint(0, 100)
    progression_step = randint(1, 10)
    position_in_progression_hide = randint(0, 9)
    limit = progression_step * 10 + number_for_progression
    progression = [x for x in
                   range(number_for_progression, limit, progression_step)]
    correct_answer = progression[position_in_progression_hide]
    progression[position_in_progression_hide] = '.'
    print(f'Question:{progression}')
    answer = string('Your answer: ')
    return answer, correct_answer
