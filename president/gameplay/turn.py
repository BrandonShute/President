from players.base_player import BasePlayer


class Turn:

    def __init__(self, player: BasePlayer):
        self.__player = player
        # TODO:brandon.shute:2018-10-04: Shuld cards_played be None
        self.__cards_played = []

    # TODO:brandon.shute:2018-10-02: Implement this fully
    def play_turn(self):
        print('Active Player is: {name}'.format(name=self.player.name))
        self.__cards_played = self.player.play_turn()

    @property
    def cards_played(self) -> list:
        return self.__cards_played

    @property
    def player(self) -> BasePlayer:
        return self.__player
