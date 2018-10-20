from unittest import TestCase

from gameplay.settings import game_settings
from gameplay.utils.cards import get_card
import gameplay.utils.card_constants as card_cons


class SettingsTest(TestCase):

    def test_when_import_game_settings_then_class_properties_are_not_null(self):
        self.assertIsNotNone(game_settings.start_card)
        self.assertIsNotNone(game_settings.trump_cards)
        self.assertIsNotNone(game_settings.card_rankings)

    def test_current_play_has_same_number_as_last_play_then_do_not_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '4'),
            get_card(card_cons.SPADES, '4'),
        ]
        last_played = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.CLUBS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

    def test_when_current_play_is_not_trump_but_different_number_than_last_play_then_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '4'),
            get_card(card_cons.DIAMONDS, '4'),
            get_card(card_cons.SPADES, '4'),
        ]
        last_played = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.CLUBS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'Expected 2 cards but 3 were played.'
        self.assertEquals(expected_error, str(context.exception))

    def test_when_current_play_is_trump_and_one_less_than_last_played_then_do_not_throw_exception(self):
        cards = [
            game_settings.trump_cards[0]
        ]
        last_played = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.CLUBS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)

    def test_when_current_play_is_trump_not_one_less_than_last_played_then_throw_exception(self):
        cards = [
            game_settings.trump_cards[0]
        ]
        last_played = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.CLUBS, '3'),
            get_card(card_cons.DIAMONDS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'When playing trump cards, you must play one less than previous play.'
        self.assertEquals(expected_error, str(context.exception))

    def test_when_playing_one_card_on_the_first_play_then_do_not_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '3'),
        ]
        last_played = None

        game_settings.validate_cards(cards, last_played)

    def test_when_playing_multiple_cards_on_the_first_play_then_do_not_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.DIAMONDS, '3'),
        ]
        last_played = None

        game_settings.validate_cards(cards, last_played)

    def test_when_new_play_has_lower_rank_than_last_play_then_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '4'),
        ]
        last_played = [
            get_card(card_cons.HEARTS, '5'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'Cannot play a lower card than the last player.'
        self.assertEquals(expected_error, str(context.exception))

    def test_when_multiple_cards_are_played_and_they_are_not_the_same_rank_then_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '4'),
            get_card(card_cons.DIAMONDS, '5'),
        ]
        last_played = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.CLUBS, '3'),
        ]

        with self.assertRaises(Exception) as context:
            game_settings.validate_cards(cards, last_played)

        expected_error = 'When playing multiple cards they must be the same rank.'
        self.assertEquals(expected_error, str(context.exception))

    def test_when_multiple_cards_are_played_and_they_are_the_same_rank_then_do_not_throw_exception(self):
        cards = [
            get_card(card_cons.HEARTS, '4'),
            get_card(card_cons.DIAMONDS, '4'),
        ]
        last_played = [
            get_card(card_cons.HEARTS, '3'),
            get_card(card_cons.CLUBS, '3'),
        ]

        game_settings.validate_cards(cards, last_played)
