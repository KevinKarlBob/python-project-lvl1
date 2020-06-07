from brain_games.cli import welcome_user
from brain_games.game_body import game_beginning
from brain_games.games.progression_game import progression_game_begin
from brain_games.scripts.brain_games import greeting


def main():
    greeting('What number is missing in the progression?')
    name = welcome_user()
    game_beginning(progression_game_begin, name)


if __name__ == '__main__':
    main()
