from .card import Card
from .action import ActionSpace
from .hand import Hand
from .deck import Deck


class Person:
    GOAL = 21

    def __init__(self, strategy=None):
        self.strategy = strategy
        self.hands = [Hand()]
        self.is_stand = False

    def reset(self):
        self.hands = [Hand()]
        self.is_stand = False

    def take(self, card: Card, num_of_hand=0):
        for h_index, hand in enumerate(self.hands):
            if h_index == num_of_hand:
                hand.put(card)

    def show(self):
        for hand in self.hands:
            hand.show()

    def __len__(self):
        return self.hands.__len__()

    def __getitem__(self, item):
        return self.hands[item]

    def make_decision(self, *args, **kwargs) -> tuple:
        pass

    def play(self, *args, **kwargs):
        pass
