from random import randint


def progression_game_begin():
    phrase = 'What number is missing in the progression?'
    number_for_progression = randint(0, 100)
    progression_step = randint(1, 10)
    position_to_hide = randint(0, 9)
    progression_length = 10
    limit = progression_step * progression_length + number_for_progression
    progression = [number for number in
                   range(number_for_progression, limit, progression_step)]
    correct_answer = progression[position_to_hide]
    progression[position_to_hide] = '.'
    return progression, correct_answer, phrase
