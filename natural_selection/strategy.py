from blackjack import Game


class Strategy:

    def __init__(self):
        self.genes = {}
        self.fitness_score = None

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
