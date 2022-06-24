from .table import Table
from .champion import ChampionSpace


class Game:
    GOAL = 21

    def __init__(self, player_strategy=None, dealer_strategy=None):
        self.table = Table(player_strategy=player_strategy, dealer_strategy=dealer_strategy)
        self.win = 0
        self.draw = 0
        self.lose = 0

    def show(self):
        print(f"WIN: {self.win}")
        print(f"DRAW: {self.draw}")
        print(f"LOSE: {self.lose}")

    def reset(self):
        self.table.reset()

    def play(self):
        self.table.play()

        self._check()

    def show_table(self):
        self.table.show()

    def _check(self):
        results = self.table.who_win()
        for result in results:
            if result == ChampionSpace.PLAYER:
                self.win += 1
            elif result == ChampionSpace.DRAW:
                self.draw += 1
            elif result == ChampionSpace.DEALER:
                self.lose += 1

    def get_rate(self, rate='win'):
        return self.__getattribute__(rate) / self.win + self.lose + self.draw
