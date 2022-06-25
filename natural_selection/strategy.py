from .blackjack import Game, ActionSpace
from random import choice, random
from copy import deepcopy


class Strategy:
    def __init__(self, p_threshold, d_threshold):
        self._p_threshold = p_threshold
        self._d_threshold = d_threshold

        self.p_decisions = {}
        self.d_decisions = {}

        self.fitness_score = None
        self._create()

    def _create(self):
        cards = ('A', '10', '9', '8', '7', '6', '5', '4', '3', '2')
        for dec in [f"{c1}_{c2}_{c3}" for c1 in cards for c2 in cards[cards.index(c1):] for c3 in cards]:
            if len(set(dec.split("_")[:-1])) == 1:
                self.p_decisions[dec] = choice([ActionSpace.SPLIT, ActionSpace.HIT, ActionSpace.STAND])
            else:
                self.p_decisions[dec] = choice([ActionSpace.HIT, ActionSpace.STAND])
        if self._p_threshold is None:
            self.p_decisions['threshold'] = choice([16, 17, 18])
        else:
            self.p_decisions['threshold'] = self._p_threshold

        self.d_decisions['threshold'] = self._d_threshold

    def __str__(self):
        return str(self.p_decisions)

    def fitness(self, number_of_games=1000, fitness_goal='win'):
        new_game = Game(self.p_decisions, self.d_decisions)
        for _ in range(number_of_games):
            new_game.play()
            new_game.reset()
        self.fitness_score = new_game.get_rate(fitness_goal)

    def mutate(self, mutation_probability):
        # TODO: implement mutate()
        pass

    def _set(self, state, decision):
        self.p_decisions[state] = decision

    def _get(self, state):
        return self.p_decisions[state]

    def crossover(self, other, cross_probability) -> tuple:
        new_1 = deepcopy(self)
        new_2 = deepcopy(other)

        for state, decision in new_1.p_decisions.items():
            if random() <= cross_probability:
                temp_decision = new_2._get(state)
                new_2._set(state, decision)
                new_1._set(state, temp_decision)
        new_1.fitness_score = None
        new_2.fitness_score = None

        return new_1, new_2
