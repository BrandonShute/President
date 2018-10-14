from gameplay.settings import game_settings
from gameplay.turn import Turn
from players.base_player import BasePlayer
from services.reducing_cycle import ReducingCycle


class Round:

    def __init__(self, players: list, start_player_index: int):
        self.turns = []
        self.round_players = ReducingCycle(players=players,
                                           start_index=start_player_index)

    def play_round(self):
        while not self.round_over:
            active_player = self.round_players.active_player
            current_turn = Turn(active_player)
            current_turn.play_turn()
            game_settings.validate_cards(current_turn.cards_played,
                                         self.last_played)
            if active_player.has_no_cards:
                self.round_players.remove_active_player()

            self.turns.append(current_turn)
            next(self.round_players)

    @property
    def last_turn(self) -> Turn:
        # TODO:brandon.shute:2018-10-14: Should these return None
        if len(self.turns) == 0:
            return None

        return self.turns[-1]

    @property
    def last_played(self) -> list:
        # TODO:brandon.shute:2018-10-14: Should these return None
        if self.last_turn is None:
            return None

        return self.last_turn.cards_played

    @property
    def last_player(self) -> BasePlayer:
        # TODO:brandon.shute:2018-10-14: Should these return None
        if self.last_turn is None:
            return None

        return self.turns[-1].player

    @property
    def round_over(self) -> bool:
        if self.last_played in game_settings.trump_cards:
            return True

        return self.round_players.active_player == self.last_player
