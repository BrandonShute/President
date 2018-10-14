from unittest import TestCase

from players.standard_player import StandardPlayer


class BasePlayerTest(TestCase):

    def test_when_instantiate_StandardPlayer_then_hand_is_not_none_and_is_computer_is_false(
            self):
        name = 'Brandon'
        player = StandardPlayer(name=name)

        self.assertEqual(name, player.name)
        self.assertEqual(False, player.is_computer)
        self.assertIsNotNone(player.cards)

    # TODO:brandon.shute:2018-10-04: Determine how to test inputs from terminal
    def test_when_play_turn_then(self):
        name = 'Brandon'
        player = StandardPlayer(name=name)
