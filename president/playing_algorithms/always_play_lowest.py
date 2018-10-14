from playing_algorithms.base_algorithm import BaseAlgorithm


class AlwaysPlayLowest(BaseAlgorithm):

    def __init__(self):
        super.__init__()

    # TODO:brandon.shute:2018-10-04: Figure out how to pass current round
    def play_turn(self, available_cards: list):
        if len(available_cards) == 0:
            return None
