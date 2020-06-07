from brain_games.cli import welcome_user
from brain_games.game_body import game_beginning
from brain_games.games.nod_game import nod_game_begin
from brain_games.scripts.brain_games import greeting


def main():
    greeting('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    game_beginning(nod_game_begin, name)


if __name__ == '__main__':
    main()
