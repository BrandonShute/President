from unittest import TestCase
from unittest import mock

from gameplay.turn import Turn
from gameplay.round import Round
from players.standard_player import StandardPlayer
from gameplay.president_card import PresidentCard
from gameplay.card_constants import HEARTS, SPADES


class TurnTest(TestCase):

    def test_when_class_is_constructed_then_class_variables_are_instantiated(self):
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]
        game_round = Round(players=players, start_player_index=0)

        self.assertEqual(0, len(game_round.turns))
        self.assertNotEqual(None, game_round.player_cycle)

    @mock.patch('gameplay.turn')
    def test_when_class_has_previous_turn_then_last_player_is_the_previous_turn_player(self, mocked_turn):
        player1 = StandardPlayer('Player1')
        mocked_turn.player.return_value = [player1]
        players = [
            player1,
            StandardPlayer('Player2'),
        ]

        game_round = Round(players=players, start_player_index=0)
        game_round.turns = [mocked_turn]
        
        self.assertEqual(player1.name, game_round.last_player.name)

    def test_when_class_has_no_previous_turn_then_last_player_is_None(self):
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]
        game_round = Round(players=players, start_player_index=0)

        self.assertEqual(None, game_round.last_player)

    @mock.patch('gameplay.turn')
    def test_when_class_has_previous_turn_then_last_turn_is_the_previous_turn(self, mocked_turn):
        cards = [PresidentCard(HEARTS, '3')]
        mocked_turn.cards_played.return_value = cards
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]

        game_round = Round(players=players, start_player_index=0)
        game_round.turns = [mocked_turn]

        self.assertEqual(cards, game_round.last_played)

    def test_when_class_has_no_previous_turn_then_last_turn_is_None(self):
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]
        game_round = Round(players=players, start_player_index=0)

        self.assertEqual(None, game_round.last_turn)


    @mock.patch('gameplay.turn')
    def test_when_class_has_previous_turn_then_last_played_is_the_previous_turn_cards(self, mocked_turn):
        mocked_turn.cards_played.return_value = [
            PresidentCard(HEARTS, '3'),
        ]
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]

        game_round = Round(players=players, start_player_index=0)
        game_round.turns = [mocked_turn]

        self.assertEqual(mocked_turn, game_round.last_turn)

    def test_when_class_has_no_previous_turn_then_last_played_is_None(self):
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]
        game_round = Round(players=players, start_player_index=0)

        self.assertEqual(None, game_round.last_played)

    @mock.patch('gameplay.turn')
    def test_when_class_has_previous_turn_then_last_played_is_the_previous_turn_cards(self, mocked_turn):
        mocked_turn.cards_played.return_value = [
            PresidentCard(HEARTS, '3'),
        ]
        players = [
            StandardPlayer('Player1'),
            StandardPlayer('Player2'),
        ]

        game_round = Round(players=players, start_player_index=0)
        game_round.turns = [mocked_turn]

        self.assertEqual(mocked_turn, game_round.last_turn)

    # 
    # @mock.patch('players.base_player')
    # def test_when_player_plays_no_cards_then_player_passed_is_true(self,
    #                                                                mocked_player):
    #     mocked_player.play_turn.return_value = []
    #     turn = Turn(player=mocked_player)
    # 
    #     turn.play_turn()
    # 
    #     self.assertEqual(True, turn.player_passed)
    #
    # @mock.patch('players.base_player')
    # def test_when_player_plays_cards_then_player_passed_is_false(self,
    #                                                              mocked_player):
    #     mocked_player.play_turn.return_value = [
    #         PresidentCard(HEARTS, '3')
    #     ]
    #     turn = Turn(player=mocked_player)
    #
    #     turn.play_turn()
    #
    #     self.assertEqual(False, turn.player_passed)
    #
    # def test_when_player_passed_is_called_before_play_turn_then_player_passed_returns_false(
    #         self):
    #     player = StandardPlayer('Brandon')
    #     turn = Turn(player=player)
    #
    #     self.assertEqual(False, turn.player_passed)
    #
    # @mock.patch('players.base_player')
    # def test_when_player_plays_cards_then_cards_played_is_updated_to_cards(self,
    #                                                                        mocked_player):
    #     cards_played = [
    #         PresidentCard(HEARTS, '3'),
    #         PresidentCard(SPADES, '3'),
    #     ]
    #     mocked_player.play_turn.return_value = cards_played
    #     turn = Turn(player=mocked_player)
    #
    #     turn.play_turn()
    #
    #     self.assertListEqual(cards_played, turn.cards_played)
