from brain_games.cli import greeting, get_answer, ask_question
from brain_games.game_factory import choose_game


def game_beginning(game_indicator):
    name = greeting(game_indicator)
    rounds_number = 3
    for i in range(rounds_number):
        data, correct_answer = choose_game(game_indicator)
        ask_question(data, game_indicator)
        answer = get_answer()
        if answer != correct_answer:
            print(f"""{answer} is wrong answer ;(. Correct answer was {correct_answer}
                        Let's try again, {name}!""")
            return
        print('Correct!')
    print(f'My Congratulations, {name}')
