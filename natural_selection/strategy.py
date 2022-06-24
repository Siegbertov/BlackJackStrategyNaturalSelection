from .blackjack import Game


cards = ('A', '10', '9', '8', '7', '6', '5', '4', '3', '2')
inputs = [f"{c1}_{c2}_{c3}" for c1 in cards for c2 in cards[cards.index(c1):] for c3 in cards]
inputs.append('threshold')
inputs.append('fitness_score')


class Strategy:
    __slots__ = tuple(inputs)

    def __init__(self):
        self._create()

    def _create(self):
        # TODO: implement _create()
        pass

    def fitness(self, number_of_games=1000, fitness_goal='win'):
        """fitness_goal => {'win', 'lose', 'draw'}"""
        new_game = Game()  # TODO pass player-strategy
        for _ in range(number_of_games):
            new_game.play()
            new_game.reset()
        self.fitness_score = new_game.get_rate(fitness_goal)

    def mutate(self, mutation_probability):
        # TODO: implement mutate()
        pass

    def crossover(self, other):
        # TODO: implement crossover()
        pass
