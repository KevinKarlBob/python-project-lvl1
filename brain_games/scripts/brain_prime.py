from brain_games.cli import welcome_user
from brain_games.games.prime_game import is_prime
from brain_games.scripts.brain_games import greeting
from brain_games.game_body import game_begining


def special_greeting():
    greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no"')


def main():
    special_greeting()
    name = welcome_user()
    game_beginning(is_prime, name)


if __name__ == '__main__':
    main()
