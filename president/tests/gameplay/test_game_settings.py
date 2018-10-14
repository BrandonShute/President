from unittest import TestCase

from gameplay.settings import game_settings


class GameSettingsTest(TestCase):

    def test_when_import_game_settings_then_start_card_is_not_None(self):
        self.assertIsNotNone(game_settings.start_card)
