from unittest import TestCase

from pyCardDeck import PokerCard

from players.standard_player import StandardPlayer


class BasePlayerTest(TestCase):

    def test_when_instantiate_StandardPlayer_then_hand_is_not_none(self):
        name = 'Brandon'
        # Used StandardPlayer to test because can't instantiate abstract class
        player = StandardPlayer(name=name)

        self.assertEqual(name, player.name)
        self.assertEqual(False, player.is_computer)
        self.assertIsNotNone(player.cards)

    def test_when_has_no_cards_with_empty_hand_then_return_true(self):
        player = StandardPlayer(name='Brandon')

        self.assertEqual(True, player.has_no_cards)

    def test_when_has_no_cards_with_populated_hand_then_return_false(self):
        card = PokerCard('Spades', '3', 'Three')
        player = StandardPlayer(name='Brandon')
        player.add_card(card)

        self.assertEqual(False, player.has_no_cards)

    def test_when_has_card_with_player_that_has_empty_hand_then_return_false(
            self):
        card = PokerCard('Spades', '3', 'Three')
        player = StandardPlayer(name='Brandon')

        self.assertEqual(False, player.has_card(card))

    def test_when_has_card_with_player_that_has_card_in_hand_then_return_true(
            self):
        card = PokerCard('Spades', '3', 'Three')
        player = StandardPlayer(name='Brandon')

        player.add_card(card)

        self.assertEqual(True, player.has_card(card))

    def test_when_has_card_with_player_with_populated_hand_but_no_card_then_return_false(
            self):
        card_in_hand = PokerCard('Spades', '3', 'Three')
        card_to_check = PokerCard('Spades', '4', 'Four')
        player = StandardPlayer(name='Brandon')

        player.add_card(card_in_hand)

        self.assertEqual(False, player.has_card(card_to_check))

    def test_when_add_cards_then_hand_contains_cards(self):
        card1 = PokerCard('Spades', '3', 'Three')
        card2 = PokerCard('Spades', '4', 'Four')
        cards_to_add = [card1, card2]

        player = StandardPlayer(name='Brandon')

        player.add_cards(cards_to_add)

        self.assertListEqual(cards_to_add, player.cards)

    def test_when_add_card_then_hand_contains_card(self):
        card = PokerCard('Spades', '3', 'Three')

        player = StandardPlayer(name='Brandon')

        player.add_card(card)

        self.assertEqual(1, len(player.cards))
        self.assertIn(card, player.cards)

    def test_when_remove_cards_that_are_in_hand_then_remove_the_cards(self):
        card1 = PokerCard('Spades', '3', 'Three')
        card2 = PokerCard('Spades', '4', 'Four')
        cards = [card1, card2]

        player = StandardPlayer(name='Brandon')

        player.add_cards(cards)

        self.assertListEqual(cards, player.cards)

        player.remove_cards(cards)

        self.assertEqual(0, len(player.cards))
        for card in cards:
            self.assertNotIn(card, player.cards)

    def test_when_remove_card_that_is_in_hand_then_remove_the_card(self):
        card = PokerCard('Spades', '3', 'Three')

        player = StandardPlayer(name='Brandon')

        player.add_card(card)

        self.assertIn(card, player.cards)

        player.remove_card(card)

        self.assertEqual(0, len(player.cards))
        self.assertNotIn(card, player.cards)

    def test_when_remove_card_that_is_not_in_hand_then_throw_exception(self):
        card = PokerCard('Spades', '3', 'Three')

        player = StandardPlayer(name='Brandon')

        with self.assertRaises(Exception) as context:
            player.remove_card(card)

        expected_error = '{} was not found in the hand.'.format(card.name)
        self.assertTrue(expected_error in str(context.exception))
