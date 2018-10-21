from gameplay.settings import game_settings
from gameplay.turn import Turn
from players.base_player import BasePlayer
from gameplay.services.reducing_cycle import ReducingCycle


class Round:

    def __init__(self, players: list, start_player_index: int):
        self.turns = []
        self.round_players = ReducingCycle(players=players,
                                           start_index=start_player_index)

    def play_round(self):
        while not self.round_over:
            self.__print_board()
            self.__print_last_play()
            active_player = self.round_players.active_player
            current_turn = Turn(active_player)
            current_turn.play_turn()

            if active_player.has_no_cards or current_turn.player_passed:
                self.round_players.remove_active_player()

            next(self.round_players)

            if not current_turn.player_passed:
                game_settings.validate_cards(current_turn.cards_played,
                                             self.last_played)
                self.turns.append(current_turn)

    @property
    def last_turn(self) -> Turn:
        if len(self.turns) == 0:
            return None

        return self.turns[-1]

    @property
    def last_played(self) -> list:
        if self.last_turn is None:
            return None

        return self.last_turn.cards_played

    @property
    def last_player(self) -> BasePlayer:
        if self.last_turn is None:
            return None

        return self.last_turn.player

    @property
    def round_over(self) -> bool:
        if self.last_played is not None and \
                self.last_played[0].president_rank == game_settings.trump_card_rank:
            return True

        return self.round_players.active_player == self.last_player

    # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    def __print_board(self):
        print('CURRENT BOARD: \n')
        for player in self.round_players.remaining_players:
            print('-----------')
            print('{name}'.format(name=player.name))
            print('-----------')
            index = 0
            for card in player.cards:
                print('{0} - {1}'.format(index, card.name))
                index += 1
            print('\n')

    # TODO:brandon.shute:2018-09-30: This will be removed, used for visualizing
    def __print_last_play(self):
        print('Last Play:')
        if self.last_turn is not None:
            [print('{card_name}'.format(card_name=card.name)) for card in
             self.last_turn.cards_played]
        print('\n')