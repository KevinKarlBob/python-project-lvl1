from brain_games.games.calc_game import calc_game_begin
from brain_games.games.ev_game import guess_even
from brain_games.games.nod_game import nod_game_begin
from brain_games.games.prime_game import is_prime
from brain_games.games.progression_game import progression_game_begin

game_dictionary = {"calc_game": ["What is the result of the expression?", calc_game_begin],
                   'even_game': ['Answer "yes" if number even otherwise answer "no"', guess_even],
                   'gcd_game': ['Find the greatest common divisor of given numbers.', nod_game_begin],
                   'prime_game': ['Answer "yes" if given number is prime. Otherwise answer "no"', is_prime],
                   'progression_game': ['What number is missing in the progression?', progression_game_begin]}


def choose_game(game_indicator):
    result = game_dictionary[game_indicator][1]()
    return result
