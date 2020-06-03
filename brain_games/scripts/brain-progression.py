from brain_games.cli import welcome_user
from brain_games.games.progression_game import progressive_game_begin
from brain_games.scripts.brain_games1 import greeting
from brain_games.game_body import game_begining


def special_greeting():
    greeting()
    print('What number is missing in the progression?')


def main():
    special_greeting()
    name = welcome_user()
    game_begining(progressive_game_begin, name)


if __name__ == '__main__':
    main()
