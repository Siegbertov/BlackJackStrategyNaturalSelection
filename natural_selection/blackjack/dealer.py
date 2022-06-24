from .person import Person, Deck, ActionSpace


class Dealer(Person):
    def __init__(self, d_strategy=None):
        super().__init__(strategy=d_strategy)

    def get_visible_card(self):
        """return first card from its hand"""
        return self.hands[0][0]

    def make_decision(self) -> tuple:
        decs = []
        for hand in self.hands:
            if hand.best_score >= self.strategy['threshold']:
                decs.append(ActionSpace.STAND)
            else:
                decs.append(ActionSpace.HIT)
        return decs, True if len(set(decs)) == 1 and decs[0] == ActionSpace.STAND else False

    def play(self, deck: Deck):
        while not self.is_stand:
            decisions, self.is_stand = self.make_decision()
            hands = self.hands
            new_hands = []

            for i, decision in enumerate(decisions):
                if decision == ActionSpace.HIT:
                    new_hand = hands[i].hit(deck)
                    new_hands.append(new_hand)
                elif decision == ActionSpace.STAND:
                    new_hand = hands[i].stand()
                    new_hands.append(new_hand)
            self.hands = new_hands
