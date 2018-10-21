from pyCardDeck import PokerCard
from gameplay.settings import game_settings
from gameplay.card_constants import SHORT_NAME_TO_LONG_NAME, SUITS


class PresidentCard(PokerCard):

    def __init__(self, suit: str, short_name: str):
        self.__validate_suit(suit)
        self.__validate_card_short_name(short_name)

        super().__init__(suit, short_name, SHORT_NAME_TO_LONG_NAME[short_name])
        self.__president_rank = game_settings.card_rankings[short_name]

    @property
    def president_rank(self):
        return self.__president_rank

    @staticmethod
    def __validate_suit(suit: str) -> None:
        # TODO:brandon.shute:2018-10-04: Give a type to this exception
        if suit not in SUITS:
            raise Exception('{0} is not a supported suit.'.format(suit))

    @staticmethod
    def __validate_card_short_name(short_name: str) -> None:
        # TODO:brandon.shute:2018-10-04: Give a type to this exception
        if short_name not in SHORT_NAME_TO_LONG_NAME.keys():
            raise Exception('There is no card for short name \"{0}\".'.format(short_name))
