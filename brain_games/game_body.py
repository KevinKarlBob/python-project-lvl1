from prompt import string
from brain_games.cli import greeting, ask_question


ROUNDS_COUNT = 3


def game_beginning(game_name):
    name = greeting(game_name)

    for i in range(ROUNDS_COUNT):
        data, correct_answer, _ = game_name()
        ask_question(data)
        answer = string("Your answer: ")
        if answer != correct_answer:
            print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}
                        Let's try again, {name}!""")
            return
        print('Correct!')
    print(f'My Congratulations, {name}')
