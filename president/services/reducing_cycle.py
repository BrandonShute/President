from itertools import cycle, islice

from players.base_player import BasePlayer


class ReducingCycle:

    def __init__(self, players: list, start_index: int = 0):
        self.__players = players
        self.__active_player = players[start_index]
        self.__players_cycle = islice(cycle(players), start_index + 1, None)

    def __next__(self) -> BasePlayer:
        self.__active_player = next(self.__players_cycle)
        return self.active_player

    @property
    def active_player(self) -> BasePlayer:
        return self.__active_player

    @property
    def remaining_players(self) -> list:
        return self.__players

    @property
    def active_position(self) -> int:
        return self.remaining_players.index(self.active_player)

    def remove_active_player(self) -> None:
        active_index = self.active_position
        self.__active_player = self.__players[active_index - 1]
        del self.__players[active_index]
        self.__players_cycle = islice(cycle(self.__players), active_index, None)
