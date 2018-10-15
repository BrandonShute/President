from pyCardDeck import PokerCard

from utils import card_constants as card_cons
from utils.cards import get_card

# TODO:brandon.shute:2018-10-04: Allow for jokers
# TODO:brandon.shute:2018-10-14: Implement turn skip for same card

START_RANK = '3'
START_CARD_SHORT_NAME = '3'
START_CARD_SUIT = card_cons.SPADES
TRUMP_CARD_SHORT_NAME = '2'


class Settings:

    def __init__(self):
        self.__start_card = get_card(START_CARD_SUIT, START_CARD_SHORT_NAME)
        self.__load_trump_cards()
        self.__load_card_rankings()

    @property
    def start_card(self) -> PokerCard:
        return self.__start_card

    @property
    def trump_cards(self) -> list:
        return self.__trump_cards

    @property
    def card_rankings(self) -> dict:
        return self.__card_rankings

    def validate_cards(self, cards: list, last_played: list) -> None:
        """
        Validates whether the new cards played are valid given the last play.
        Throws an exception if the cards are no valid

        :param cards: A list of PokerCards representing the new play
        :param last_played: A list of PokerCards representing the last play
        :return: None
        """
        # The player passes
        if len(cards) == 0:
            return

        if len(cards) > 1:
            self.__validate_multiple_card_played(cards)

        # First play of game
        if last_played is None:
            return

        self.__validate_number_of_cards_played(cards, last_played)
        self.__validate_card_ranks(cards, last_played)

    def __load_trump_cards(self) -> None:
        self.__trump_cards = []
        for suit in card_cons.SUITS:
            self.__trump_cards.append(get_card(suit, TRUMP_CARD_SHORT_NAME))

    def __load_card_rankings(self):
        # TODO:brandon.shute:2018-10-14: Implement this method generically
        # from start card.
        self.__card_rankings = {
            '3': 0,
            '4': 1,
            '5': 2,
            '6': 3,
            '7': 4,
            '8': 5,
            '9': 6,
            '10': 7,
            'J': 8,
            'Q': 9,
            'K': 10,
            'A': 11,
            '2': 12
        }

    def __validate_number_of_cards_played(self, cards_played: list,
                                          last_played: list) -> None:
        num_played = len(cards_played)
        num_played_last = len(last_played)

        if num_played == 0 or num_played == num_played_last:
            return

        if cards_played in self.trump_cards and num_played == (
                num_played_last - 1):
            return

        raise Exception(
            'Expected {num_expected} cards but {num_played} were played.'.format(
                num_expected=len(last_played), num_played=num_played))

    @staticmethod
    def __validate_multiple_card_played(cards_played: list) -> None:
        first_played_rank = cards_played[0].rank
        for card in cards_played:
            if card.rank is not first_played_rank:
                raise Exception(
                    'When playing multiple cards they must be the same rank.')

        return

    def __validate_card_ranks(self, cards: list, last_played: list) -> None:
        # Only check the first card because we have validated that they are
        # all the same already
        first_card_rank = self.__card_rankings[cards[0].rank]
        first_last_played_rank = self.__card_rankings[last_played[0].rank]
        if first_card_rank < first_last_played_rank:
            raise Exception('Cannot play a lower card than the last player')


game_settings = Settings()
