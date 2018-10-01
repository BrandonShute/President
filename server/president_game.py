
from pyCardDeck import Deck
from pyCardDeck import PokerCard
# TODO:brandon.shute:2018-09-30: Add typing
# from typing import List


START_CARD = PokerCard('Spades', '3', 'Three')


class PresidentGame:

    def __init__(self, players: list):
        # TODO:brandon.shute:2018-09-30: Implement many decks for big games
        self.deck = Deck()
        self.players = players
        self.__dealer_index = 0
        self.__active_player_index = 0
        self.__remaining_players = players.copy()
        self.__generate_deck()
        # TODO:brandon.shute:2018-09-30: Need to manage played cards after rules
        self.__last_play = []
        print("Created a game with {} players.".format(len(self.players)))

    def deal(self):
        self.deck.shuffle()
        player_index = self.__get_next_player_index(self.__dealer_index)
        while not self.deck.empty:
            self.players[player_index].hand.add_card(self.deck.draw())
            player_index = self.__get_next_player_index(player_index)

        self.__active_player_index = self.__get_starting_player_index()
        self.__update_dealer()
        self.__print_board()

    def start_game(self):
        while not self.__game_over():
            self.__play_turn()
            self.__print_board()
            self.__print_last_play()

    @property
    def active_player(self):
        return self.__remaining_players[self.__active_player_index]

    def __play_turn(self):
        player = self.active_player
        print('Active Player is: {name}'.format(name=player.name))
        played_cards = player.play_turn()

        # TODO:brandon.shute:2018-09-30: Implement validation

        # TODO:brandon.shute:2018-09-30: add method for this
        if len(player.hand.cards) == 0:
            self.__remaining_players.remove(player)
        else:
            self.__active_player_index = self.__get_next_player_index(
                self.__active_player_index)

        self.__last_play = played_cards

    def __game_over(self) -> bool:
        return len(self.__remaining_players) == 0

    def __get_next_player_index(self, current_index: int) -> int:
        if current_index < len(self.__remaining_players) - 1:
            return current_index + 1

        return 0

    def __update_dealer(self) -> None:
        self.__dealer_index = self.__get_next_player_index(self.__dealer_index)

    def __get_starting_player_index(self) -> int:
        for player_index in range(len(self.players)):
            if self.players[player_index].has_card(START_CARD):
                return player_index

    def __generate_deck(self) -> None:
        # TODO:brandon.shute:2018-09-30: Generate myself to set ranking
        self.deck.load_standard_deck()
        # TODO:brandon.shute:2018-09-30: Add ability to have jokers

    def __validate_number_of_cards_played(self, cards_played) -> None:
        num_cards_to_play = len(self.__last_play)
        num_cards_played = len(cards_played)
        if num_cards_to_play is not num_cards_played:
            raise('{expected_number} cards need to be played but {actual_number} were played.'.format(expected_number=num_cards_to_play, actual_number=cards_played))


    # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    def __print_board(self):

        print('CURRENT BOARD: \n')
        for player in self.players:
            print('-----------')
            print('{name}'.format(name=player.name))
            print('-----------')
            [print('{card_name}'.format(card_name=card.name)) for card in
             player.hand.cards]
            print('\n')

    # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    def __print_last_play(self):

        print('Last Play:')
        [print('{card_name}'.format(card_name=card.name)) for card in
             self.__last_play]


if __name__ == '__main__':
    from standard_player import StandardPlayer
    from computer_player import ComputerPlayer
    _players = [
        StandardPlayer('Brandon'), StandardPlayer('Emily'), StandardPlayer('JP'),
        StandardPlayer('Kate'), StandardPlayer('Bridget')
    ]
    president = PresidentGame(_players)
    president.deal()

    president.start_game()
