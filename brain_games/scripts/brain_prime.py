from brain_games.cli import welcome_user
from brain_games.game_body import game_beginning
from brain_games.games.prime_game import is_prime
from brain_games.scripts.brain_games import greeting


def main():
    greeting('Answer "yes" if given number is prime. Otherwise answer "no"')
    name = welcome_user()
    game_beginning(is_prime, name)


if __name__ == '__main__':
    main()
