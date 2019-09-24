from gameplay.settings import game_settings
from gameplay.turn import Turn
from players.base_player import BasePlayer
from gameplay.services.reducing_cycle import ReducingCycle


class Round:

    def __init__(self, players: list, start_player_index: int):
        self.turns = []
        self.player_cycle = ReducingCycle(players=players.copy(),
                                          start_index=start_player_index)

    def play_round(self):
        while not self.round_over:
            # self.__print_board()
            # self.__print_last_play()
            active_player = self.player_cycle.active_player
            current_turn = Turn(active_player)
            current_turn.play_turn()

            if current_turn.player_passed:
                self.player_cycle.remove_active_player()

            if not current_turn.player_passed:
                game_settings.validate_cards(current_turn.cards_played,
                                             self.last_played)
                self.turns.append(current_turn)

            if active_player.has_no_cards:
                self.player_cycle.remove_active_player()

            next(self.player_cycle)

    @property
    def last_turn(self) -> Turn:
        if self.__is_first_turn():
            return None
        return self.turns[-1]

    @property
    def last_played(self) -> list:
        return self.last_turn.cards_played
        if self.__is_first_turn:
            return None
        return self.last_turn.cards_played

    @property
    def last_player(self) -> BasePlayer:
        if self.__is_first_turn():
            return None
        return self.last_turn.player

    @property
    def round_over(self) -> bool:
        if not self.__is_first_turn() and \
                game_settings.is_trump_card(self.last_played[0]):
            return True
        return self.player_cycle.active_player == self.last_player

    def __is_first_turn(self):
        return len(self.turns) == 0

    # # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    # def __print_board(self):
    #     print('CURRENT BOARD: \n')
    #     for player in self.player_cycle.remaining_players:
    #         print('-----------')
    #         print('{name}'.format(name=player.name))
    #         print('-----------')
    #         index = 0
    #         for card in player.cards:
    #             print('{0} - {1}'.format(index, card.name))
    #             index += 1
    #         print('\n')
    #
    # # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    # def __print_last_play(self):
    #     print('Last Play:')
    #     if self.last_turn is not None:
    #         [print('{card_name}'.format(card_name=card.name)) for card in
    #          self.last_turn.cards_played]
    #     print('\n')