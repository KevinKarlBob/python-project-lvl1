from brain_games.constants import game_dictionary


def choose_game(game_indicator):
    result = game_dictionary[game_indicator]()
    return result
