from players.base_player import BasePlayer
from playing_algorithms.base_algorithm import BaseAlgorithm


# TODO:brandon.shute:2018-10-14: Implement a default algo when built out


class ComputerPlayer(BasePlayer):

    def __init__(self, name: str, playing_algo: BaseAlgorithm = None):
        super().__init__(name=name, is_computer=True)
        self.__playing_algo = playing_algo

    def play_turn(self):
        # TODO:brandon.shute:2018-09-30: Implement
        pass
