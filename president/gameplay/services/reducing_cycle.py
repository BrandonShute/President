from itertools import cycle, islice

from players.base_player import BasePlayer


class ReducingCycle:
    """
    This is a generic implementation of a cycle which can reduce in size.
    """

    def __init__(self, players: list, start_index: int = 0):
        self.__players = players
        self.__set_active_player(start_index)

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
        self.__set_active_player(active_index - 1)
        del self.__players[active_index]

    def __set_active_player(self, index: int) -> None:
        try:
            self.__active_player = self.__players[index]
            self.__players_cycle = islice(cycle(self.__players), index + 1, None)
        except IndexError:
            num_players = len(self.__players)
            message = 'Cannot set start index to {} when Cycle has {} players.'\
                .format(index, num_players)
            raise IndexError(message)
