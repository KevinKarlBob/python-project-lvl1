from operator import add, sub, mul
from brain_games.games.calc_game import calc_game_begin
from brain_games.games.ev_game import guess_even
from brain_games.games.nod_game import nod_game_begin
from brain_games.games.prime_game import is_prime
from brain_games.games.progression_game import progression_game_begin

game_dictionary = {"calc_game":  calc_game_begin,
                   'even_game': guess_even,
                   'gcd_game':  nod_game_begin,
                   'prm_game':  is_prime,
                   'progression_game': progression_game_begin}

phrase_dictionary = {
    "calc_game": "What is the result of the expression?",
    'even_game': 'Answer "yes" if number even otherwise answer "no"',
    'gcd_game': 'Find the greatest common divisor of given numbers.',
    'prm_game': 'Answer "yes" if given number is prime. Otherwise answer "no"',
    'progression_game': 'What number is missing in the progression?'
    }

transfer_math_operators = {'+': add, '-': sub, '*': mul}
