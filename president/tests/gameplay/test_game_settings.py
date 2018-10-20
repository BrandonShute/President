from unittest import TestCase

from gameplay.settings import game_settings


class GameSettingsTest(TestCase):

    def test_when_import_game_settings_then_class_properties_are_not_null(self):
        self.assertIsNotNone(game_settings.start_card)
        self.assertIsNotNone(game_settings.trump_cards)
        self.assertIsNotNone(game_settings.card_rankings)

    def test_current_play_has_same_number_as_last_play_then_do_not_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_when_current_play_is_not_trump_but_different_number_than_last_play_then_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_when_current_play_is_trump_and_one_less_than_last_played_then_do_not_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_current_play_is_trump_not_one_less_than_last_played_then_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_playing_one_card_on_first_play_does_not_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_playing_multiple_cards_on_first_play_does_not_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_when_new_play_has_lower_rank_than_last_play_then_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)

    def test_when_multiple_cards_are_played_and_they_are_not_the_same_then_throw_exception(self):
        self.assertIsNotNone(game_settings.start_card)
