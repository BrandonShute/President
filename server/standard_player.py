from base_player import BasePlayer


QUIT_STRING = 'q'


class StandardPlayer(BasePlayer):

    def __init__(self, name: str):
        super().__init__(name=name)

    def play_turn(self) -> list:
        # TODO:brandon.shute:2018-09-30: Use name instead of index
        played_cards = []
        finished = False
        while not finished:
            passed_input = input(
                "Enter a card index to play (or q to end the turn): "
            )
            if passed_input == QUIT_STRING:
                break

            # TODO:brandon.shute:2018-09-30: Add a remove for index
            played_cards.append(self.hand.cards[int(passed_input)])

        self.hand.remove_cards(played_cards)
        return played_cards
