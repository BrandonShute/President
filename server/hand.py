from pyCardDeck.cards import PokerCard


class Hand:

    def __init__(self):
        self.cards = []

    def add_cards(self, cards_to_add: list) -> None:
        self.cards.extend(cards_to_add)

    def add_card(self, card_to_add: PokerCard) -> None:
        self.add_cards([card_to_add])

    def remove_card(self, card_to_remove: PokerCard) -> None:
        try:
            self.cards.remove(card_to_remove)
        except ValueError:
            raise Exception('{card_name} was not found in the hand.'.format(card_name=card.name))

    def remove_cards(self, cards_to_remove: list) -> None:
        for card in cards_to_remove:
            self.remove_card(card)

    def organize_cards(self, descending_order: bool=False) -> None:
        # TODO:brandon.shute:2018-09-30: Sort based on president card ordering
        self.cards.sort(reverse=descending_order)
