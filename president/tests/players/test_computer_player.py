from unittest import TestCase

from players.computer_player import ComputerPlayer


class BasePlayerTest(TestCase):

    def test_when_instantiate_ComputerPlayer_then_hand_is_not_none_and_is_computer_is_true(
            self):
        name = 'Brandon'
        player = ComputerPlayer(name=name)

        self.assertEqual(name, player.name)
        self.assertEqual(True, player.is_computer)
        self.assertIsNotNone(player.cards)
