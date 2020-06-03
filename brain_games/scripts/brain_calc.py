from brain_games.cli import welcome_user
from brain_games.games.calc_game import calc_game_begin
from brain_games.scripts.brain_games1 import greeting
from brain_games.game_body import game_begining


def special_greeting():
    greeting()
    print('What is the result of the expression?')


def main():
    special_greeting()
    name = welcome_user()
    game_begining(calc_game_begin, name)


if __name__ == '__main__':
    main()
