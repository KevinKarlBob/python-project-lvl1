from brain_games.games.calc_game import calc_game_begin
from brain_games.games.ev_game import guess_even
from brain_games.games.nod_game import nod_game_begin
from brain_games.games.prime_game import prime_game_begin
from brain_games.games.progression_game import progression_game_begin

GAME_DICTIONARY = {"calc_game": calc_game_begin,
                   'even_game': guess_even,
                   'gcd_game': nod_game_begin,
                   'prm_game': prime_game_begin,
                   'progression_game': progression_game_begin}


def choose_game(game_indicator):
    result = GAME_DICTIONARY[game_indicator]()
    return result
