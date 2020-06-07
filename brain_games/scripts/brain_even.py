from brain_games.game_body import game_beginning
from brain_games.games.ev_game import guess_even
from brain_games.scripts.brain_games import greeting
from brain_games.scripts.brain_games import welcome_user


def main():
    greeting('Answer "yes" if number even otherwise answer "no"')
    name = welcome_user()
    game_beginning(guess_even, name)


if __name__ == '__main__':
    main()
