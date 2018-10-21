from unittest import TestCase

from gameplay.president_card import PresidentCard
from gameplay.card_constants import HEARTS


class PresidentCardTest(TestCase):

    def test_when_initalize_PresidentCard_for_valid_suit_and_shot_name_then_card_is_created(self):
        suit = HEARTS
        short_name = '2'

        card = PresidentCard(suit, short_name)

        self.assertNotEqual(None, card.president_rank)

    def test_when_initalize_PresidentCard_for_invalid_suit_then_throw_exception(self):
        suit = 'FAKE SUIT'
        short_name = '2'

        with self.assertRaises(Exception) as context:
            PresidentCard(suit, short_name)

        expected_error = 'FAKE SUIT is not a supported suit.'
        self.assertEqual(expected_error, str(context.exception))

    def test_when_initalize_PresidentCard_for_invalid_short_name_then_throw_exception(self):
        suit = HEARTS
        short_name = 'Invalid Name'

        with self.assertRaises(Exception) as context:
            PresidentCard(suit, short_name)

        expected_error = 'There is no card for short name \"Invalid Name\".'
        self.assertEqual(expected_error, str(context.exception))
