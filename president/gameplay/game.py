from pyCardDeck import Deck

from gameplay.hand import Hand
from gameplay.settings import game_settings
from gameplay.services.reducing_cycle import ReducingCycle


# TODO:brandon.shute:2018-09-30: Add typing
# from typing import List


class Game:

    def __init__(self, players: list, num_deals_per_player: int = 3):
        # TODO:brandon.shute:2018-10-04: Deck should be managed in GameHand
        # TODO:brandon.shute:2018-09-30: Implement many decks for big games
        # TODO:brandon.shute:2018-10-03: Move deck down to Hand
        self.deck = Deck()
        self.players = players
        self.__dealer_cycle = ReducingCycle(players=players, start_index=0)
        self.hands = []
        self.__num_hands_to_play = num_deals_per_player * len(players)
        self.__generate_deck()
        print("Created a game with {} players.".format(len(self.players)))

    def play_game(self):
        while not self.game_over:
            current_hand = Hand(self.players, self.__get_hand_starting_index())
            current_hand.play_hand()
            self.hands.append(current_hand)

    def deal(self):
        self.deck.shuffle()
        player_dealing_cycle = ReducingCycle(players=self.players,
                                             start_index=self.__dealer_cycle.active_position + 1)
        while not self.deck.empty:
            player_dealing_cycle.active_player.add_card(self.deck.draw())
            next(player_dealing_cycle)

        self.__organize_player_cards()

        # TODO:brandon.shute:2018-10-04: Implement hand sorting
        # for player in self.players:
        #     player.organize_cards()

        next(self.__dealer_cycle)

    @property
    def game_over(self) -> bool:
        return self.__num_hands_to_play < len(self.hands)

    def __generate_deck(self) -> None:
        # TODO:brandon.shute:2018-09-30: Generate myself to set ranking
        self.deck.load_standard_deck()  # TODO:brandon.shute:2018-09-30: Add ability to have jokers

    def __get_hand_starting_index(self):
        if len(self.hands) == 0:
            return self.__get_player_with_start_card()

        # TODO:brandon.shute:2018-10-02: Implment based on results of last round
        return self.__dealer_cycle.active_position

    def __get_player_with_start_card(self):
        player_index = 0
        for player in self.players:
            if game_settings.start_card in player.cards:
                return player_index
            player_index += 1

        raise Exception(
            'No player had the start card specified in the game settings: {start_card}'.format(
                start_card=game_settings.start_card.name))

    def __organize_player_cards(self):
        for player in self.players:
            player.organize_cards()


if __name__ == '__main__':
    from players.standard_player import StandardPlayer

    players = [StandardPlayer('Brandon'), StandardPlayer('Emily'),
               StandardPlayer('JP'), StandardPlayer('Kate'),
               StandardPlayer('Bridget')]
    president = Game(players)
    president.deal()
    president.play_game()
