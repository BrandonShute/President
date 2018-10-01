from base_player import BasePlayer


class ComputerPlayer(BasePlayer):

    def __init__(self, name: str):
        super().__init__(name=name, is_computer=True)

    def play_turn(self):
        # TODO:brandon.shute:2018-09-30: Implement
        pass
