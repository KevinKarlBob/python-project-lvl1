from brain_games.cli import welcome_user
from brain_games.game_body import game_beginning
from brain_games.games.calc_game import calc_game_begin
from brain_games.scripts.brain_games import greeting


def main():
    greeting('What is the result of the expression?')
    name = welcome_user()
    game_beginning(calc_game_begin, name)


if __name__ == '__main__':
    main()
