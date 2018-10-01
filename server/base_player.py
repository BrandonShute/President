from abc import ABC, abstractmethod
from hand import Hand
from pyCardDeck import PokerCard


class BasePlayer(ABC):

    def __init__(self, name: str, is_computer: bool=False):
        self.name = name
        self.is_computer = is_computer
        self.hand = Hand()

    def has_card(self, card: PokerCard) -> bool:
        for hand_card in self.hand.cards:
            if hand_card == card:
                return True

        return False

    @abstractmethod
    def play_turn(self):
        pass
