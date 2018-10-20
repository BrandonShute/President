from pyCardDeck import PokerCard

from gameplay.utils import card_constants as card_cons


def get_card(suit: str, card_short_name: str) -> PokerCard:
    validate_suit(suit)
    validate_card_short_name(card_short_name)
    card_long_name = card_cons.SHORT_NAME_TO_LONG_NAME[card_short_name]
    return PokerCard(suit, card_short_name, card_long_name)


def validate_suit(suit: str) -> None:
    # TODO:brandon.shute:2018-10-04: Give a type to this exception
    if suit not in card_cons.SUITS:
        raise Exception('{suit} is not a supported suit.'.format(suit=suit))


def validate_card_short_name(short_name: str) -> None:
    # TODO:brandon.shute:2018-10-04: Give a type to this exception
    if short_name not in card_cons.SHORT_NAME_TO_LONG_NAME.keys():
        raise Exception('There is no card for short name \"{name}\".'.format(
            name=short_name))
