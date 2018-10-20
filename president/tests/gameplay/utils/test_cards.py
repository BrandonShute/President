from unittest import TestCase

from pyCardDeck import PokerCard
from gameplay.utils import card_constants as card_cons
from gameplay.utils.cards import get_card


class CardsTest(TestCase):

    def test_when_get_card_for_valid_suit_and_shot_name_then_return_card(self):
        suit = card_cons.HEARTS
        short_name = '2'
        long_name = card_cons.SHORT_NAME_TO_LONG_NAME[short_name]

        expected_card = PokerCard(suit, short_name, long_name)

        card = get_card(suit, short_name)

        self.assertEqual(expected_card, card)

    def test_when_get_card_for_invalid_suit_then_throw_exception(self):
        suit = 'FAKE SUIT'
        short_name = '2'

        with self.assertRaises(Exception) as context:
            get_card(suit, short_name)

        expected_error = 'FAKE SUIT is not a supported suit.'
        self.assertEquals(expected_error, str(context.exception))

    def test_when_get_card_for_invalid_short_name_then_throw_exception(self):
        suit = card_cons.HEARTS
        short_name = 'Invalid Name'

        with self.assertRaises(Exception) as context:
            get_card(suit, short_name)

        expected_error = 'There is no card for short name \"Invalid Name\".'
        self.assertEquals(expected_error, str(context.exception))
