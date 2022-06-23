class Strategy:

    def __init__(self):
        self.genes = {}
        self.fitness_score = None

        self._create()

    def _create(self):
        # TODO: implement _create()
        pass

    def fitness(self):
        # TODO: implement fitness()
        """updates fitness_score"""
        pass

    def mutate(self, mutation_probability):
        # TODO: implement mutate()
        pass

    def crossover(self, other):
        # TODO: implement crossover()
        pass
