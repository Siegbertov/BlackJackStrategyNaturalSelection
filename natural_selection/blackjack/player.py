from .person import Person, Deck, Card, ActionSpace  # imported DECK with annotation purposes


class Player(Person):
    def __init__(self, p_strategy=None):
        super().__init__(strategy=p_strategy)

    def make_decision(self, visible_card: Card) -> tuple:
        decs = []
        for hand in self.hands:
            state = []
            for card in hand.cards:
                if card.rank in ("J", "Q", "K"):
                    state.append("10")
                else:
                    state.append(card.rank)
            state = sorted(state, key=lambda x: ('A', '10', '9', '8', '7', '6', '5', '4', '3', '2').index(x))

            if visible_card.rank in ("J", "Q", "K"):
                state.append('10')
            else:
                state.append(visible_card.rank)

            current_question = "_".join(state)

            if current_question in self.strategy:
                decs.append(self.strategy[current_question])
            elif hand.best_score >= self.strategy["threshold"]:
                decs.append(ActionSpace.STAND)
            else:
                decs.append(ActionSpace.HIT)
        return decs, True if len(set(decs)) == 1 and decs[0] == ActionSpace.STAND else False

    def play(self, deck: Deck, card: Card):
        while not self.is_stand:
            decisions, self.is_stand = self.make_decision(visible_card=card)
            hands = self.hands
            new_hands = []

            for i, decision in enumerate(decisions):
                if decision == ActionSpace.SPLIT:
                    new_hand = hands[i].split(deck)
                    new_hands.append(new_hand[0])
                    new_hands.append(new_hand[1])
                elif decision == ActionSpace.HIT:
                    new_hand = hands[i].hit(deck)
                    new_hands.append(new_hand)
                elif decision == ActionSpace.STAND:
                    new_hand = hands[i].stand()
                    new_hands.append(new_hand)
            self.hands = new_hands
