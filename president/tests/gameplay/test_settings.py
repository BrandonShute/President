from unittest import TestCase

from gameplay.settings import game_settings, TRUMP_CARD_SHORT_NAME
from gameplay.settings import START_CARD_SUIT, START_CARD_SHORT_NAME
from gameplay.president_card import PresidentCard
from gameplay.card_constants import SPADES, CLUBS, HEARTS, DIAMONDS


class SettingsTest(TestCase):

    def test_when_import_game_settings_then_class_properties_are_not_null(self):
        self.assertIsNotNone(game_settings.trump_card_rank)
        self.assertIsNotNone(game_settings.card_rankings)

    def test_current_play_has_same_number_as_last_play_then_do_not_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '4'),
            PresidentCard(SPADES, '4'),
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(CLUBS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

    def test_when_current_play_is_not_trump_but_different_number_than_last_play_then_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '4'),
            PresidentCard(DIAMONDS, '4'),
            PresidentCard(SPADES, '4'),
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(CLUBS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'Expected 2 cards but 3 were played.'
        self.assertEqual(expected_error, str(context.exception))

    def test_when_current_play_is_trump_and_one_less_than_last_played_then_do_not_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, TRUMP_CARD_SHORT_NAME)
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(CLUBS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

    def test_when_last_play_is_one_card_and_one_trump_card_is_played_then_do_not_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, TRUMP_CARD_SHORT_NAME),
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

    def test_when_last_play_is_more_than_one_card_and_same_number_of_trumps_played_then_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, TRUMP_CARD_SHORT_NAME),
            PresidentCard(DIAMONDS, TRUMP_CARD_SHORT_NAME),
        ]
        last_played = [
            PresidentCard(CLUBS, '3'),
            PresidentCard(DIAMONDS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'When playing trump cards, you must play one less than previous play.'
        self.assertEqual(expected_error, str(context.exception))

    def test_when_last_play_is_three_card_and_current_play_is_one_trump_then_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, TRUMP_CARD_SHORT_NAME)
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(CLUBS, '3'),
            PresidentCard(DIAMONDS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'When playing trump cards, you must play one less than previous play.'
        self.assertEqual(expected_error, str(context.exception))

    def test_when_playing_one_card_on_the_first_play_then_do_not_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '3'),
        ]
        last_played = None

        game_settings.validate_cards(cards, last_played)

    def test_when_playing_multiple_cards_on_the_first_play_then_do_not_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(DIAMONDS, '3'),
        ]
        last_played = None

        game_settings.validate_cards(cards, last_played)

    def test_when_new_play_has_lower_rank_than_last_play_then_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '4'),
        ]
        last_played = [
            PresidentCard(HEARTS, '5'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'Cannot play a lower card than the last player.'
        self.assertEqual(expected_error, str(context.exception))

    def test_when_multiple_cards_are_played_and_they_are_not_the_same_rank_then_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '4'),
            PresidentCard(DIAMONDS, '5'),
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(CLUBS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'When playing multiple cards they must be the same rank.'
        self.assertEqual(expected_error, str(context.exception))

    def test_when_multiple_cards_are_played_and_they_are_the_same_rank_then_do_not_throw_exception(self):
        cards = [
            PresidentCard(HEARTS, '4'),
            PresidentCard(DIAMONDS, '4'),
        ]
        last_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(CLUBS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

    def test_passed_start_card_then_is_start_card_returns_true(self):
        card = PresidentCard(START_CARD_SUIT, START_CARD_SHORT_NAME)

        result = game_settings.is_start_card(card)

        self.assertEqual(True, result)

    def test_passed_card_with_different_suit_then_is_start_card_returns_false(self):
        card = PresidentCard(HEARTS, START_CARD_SHORT_NAME)

        result = game_settings.is_start_card(card)

        self.assertEqual(False, result)

    def test_when_sort_multiple_president_cards_then_should_sort_by(self):
        card = PresidentCard(START_CARD_SUIT, '7')

        result = game_settings.is_start_card(card)

        self.assertEqual(False, result)

    def test_when_validate_cards_for_no_cards_played_then_do_not_throw_exception(self):
        cards = []
        last_played = [
            PresidentCard(HEARTS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

