from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):

    def __init__(self):
        pass

    # TODO:brandon.shute:2018-10-04: Figure out how to pass current round
    @abstractmethod
    def play_turn(self, available_cards: list):
        if len(available_cards) == 0:
            return None
