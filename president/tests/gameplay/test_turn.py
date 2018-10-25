from unittest import TestCase
from unittest import mock

from gameplay.turn import Turn
from players.standard_player import StandardPlayer
from gameplay.president_card import PresidentCard
from gameplay.card_constants import HEARTS, SPADES


class TurnTest(TestCase):

    def test_when_class_is_constructed_then_player_is_not_None(self):
        player = StandardPlayer('Brandon')
        turn = Turn(player=player)

        self.assertNotEqual(None, turn.player)
        
    @mock.patch('players.base_player')
    def test_when_play_turn_then_players_play_is_called(self, mocked_player):
        mocked_player.play_turn.return_value = []
        turn = Turn(player=mocked_player)

        turn.play_turn()

        mocked_player.play_turn.assert_called()
    
    @mock.patch('players.base_player')
    def test_when_player_plays_no_cards_then_player_passed_is_true(self, mocked_player):
        mocked_player.play_turn.return_value = []
        turn = Turn(player=mocked_player)

        turn.play_turn()

        self.assertEqual(True, turn.player_passed)

    @mock.patch('players.base_player')
    def test_when_player_plays_cards_then_player_passed_is_false(self, mocked_player):
        mocked_player.play_turn.return_value = [
            PresidentCard(HEARTS, '3')
        ]
        turn = Turn(player=mocked_player)

        turn.play_turn()

        self.assertEqual(False, turn.player_passed)
    
    def test_when_player_passed_is_called_before_play_turn_then_player_passed_returns_false(self):
        player = StandardPlayer('Brandon')
        turn = Turn(player=player)

        self.assertEqual(False, turn.player_passed)
    
    @mock.patch('players.base_player')
    def test_when_player_plays_cards_then_cards_played_is_updated_to_cards(self, mocked_player):
        cards_played = [
            PresidentCard(HEARTS, '3'),
            PresidentCard(SPADES, '3'),
        ]
        mocked_player.play_turn.return_value = cards_played
        turn = Turn(player=mocked_player)

        turn.play_turn()

        self.assertListEqual(cards_played, turn.cards_played)
