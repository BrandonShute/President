from players.base_player import BasePlayer


class Turn:

    def __init__(self, player: BasePlayer):
        self.__player = player
        self.__cards_played = None

    def play_turn(self):
        # TODO:brandon.shute:2018-10-24: Remove print after UI is built
        print('Active Player is: {name}'.format(name=self.player.name))
        self.__cards_played = self.player.play_turn()

    @property
    def cards_played(self) -> list:
        return self.__cards_played

    @property
    def player(self) -> BasePlayer:
        return self.__player

    @property
    def player_passed(self) -> BasePlayer:
        return self.cards_played == []
