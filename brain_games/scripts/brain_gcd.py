from brain_games.cli import welcome_user
from brain_games.games.nod_game import nod_game_begin
from brain_games.scripts.brain_games import greeting
from brain_games.game_body import game_begining


def special_greeting():
    greeting()
    print('Find the greatest common divisor of given numbers.')


def main():
    special_greeting()
    name = welcome_user()
    game_begining(nod_game_begin, name)


if __name__ == '__main__':
    main()
