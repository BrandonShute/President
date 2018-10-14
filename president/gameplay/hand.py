from gameplay.round import Round
from players.base_player import BasePlayer


class Hand:

    def __init__(self, players: list, start_player_index: int):
        self.__players = players
        self.__game_start_index = start_player_index
        self.rounds = []

    def play_hand(self):
        while not self.hand_over:
            self.__print_board()
            current_round = Round(players=self.remaining_players,
                                  start_player_index=self.__get_round_starting_index())
            current_round.play_round()
            self.rounds.append(current_round)
            self.__print_last_play()

    @property
    def last_round(self) -> Round:
        if len(self.rounds) == 0:
            return None

        return self.rounds[-1]

    @property
    def remaining_players(self) -> list:
        if self.last_round is None:
            return self.__players

        return self.last_round.round_players.remaining_players

    @property
    def last_round_winner(self) -> BasePlayer:
        if self.last_round is None:
            return None

        return self.last_round.last_player

    @property
    def hand_over(self) -> bool:
        return len(self.remaining_players) == 1

    def __get_round_starting_index(self):
        if self.last_round is None:
            return self.__game_start_index
        elif self.last_round_winner in self.remaining_players:
            return self.remaining_players.index(self.last_round_winner)

        # TODO:brandon.shute:2018-10-02: Find the index of the next player if the winner is out
        return 0

    # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    def __print_board(self):
        print('CURRENT BOARD: \n')
        for player in self.__players:
            print('-----------')
            print('{name}'.format(name=player.name))
            print('-----------')
            [print('{card_name}'.format(card_name=card.name)) for card in
             player.cards]
            print('\n')

    # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    def __print_last_play(self):
        print('Last Play:')
        [print('{card_name}'.format(card_name=card.name)) for card in
         self.last_round.last_turn.cards_played]
