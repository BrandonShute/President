from abc import ABC, abstractmethod

from pyCardDeck import PokerCard


class BasePlayer(ABC):

    def __init__(self, name: str, is_computer: bool = False):
        self.name = name
        self.is_computer = is_computer
        self.__cards = []

    @property
    def cards(self) -> list:
        return self.__cards

    @property
    def has_no_cards(self) -> bool:
        return len(self.cards) == 0

    @abstractmethod
    def play_turn(self):
        pass

    def has_card(self, card: PokerCard) -> bool:
        for hand_card in self.cards:
            if hand_card == card:
                return True

        return False

    def add_cards(self, cards_to_add: list) -> None:
        self.__cards.extend(cards_to_add)

    def add_card(self, card_to_add: PokerCard) -> None:
        self.add_cards([card_to_add])

    def remove_card(self, card_to_remove: PokerCard) -> None:
        try:
            self.__cards.remove(card_to_remove)
        except ValueError:
            raise Exception('{} was not found in the hand.'
                            .format(card_to_remove.name))

    def remove_cards(self, cards_to_remove: list) -> None:
        for card in cards_to_remove:
            self.remove_card(card)

    # TODO:brandon.shute:2018-09-30: Sort based on president card ordering
    def organize_cards(self, descending_order: bool = False) -> None:
        pass
