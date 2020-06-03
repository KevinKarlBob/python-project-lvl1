from brain_games.scripts.brain_games1 import welcome_user
from brain_games.game_body import game_begining
from brain_games.scripts.brain_games1 import greeting
from brain_games.games.evgame import guess_even


def special_greeting():
    greeting()
    print('Answer "yes" if number even otherwise answer "no"')


def main():
    special_greeting()
    name = welcome_user()
    game_begining(guess_even, name)


if __name__ == '__main__':
    main()
