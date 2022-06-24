from .strategy import Strategy


class Evolution:
    __slots__ = ('dealer_threshold', 'population', 'population_size', 'number_of_generations', 'p_cross', 'p_mut', '__current_epoch', '__was_changed')

    def __init__(self, dealer_threshold=None, population_size=None, number_of_generations=None, p_cross=None, p_mut=None):
        self.__current_epoch = 0
        self.__was_changed = False
        self.population = []

        if dealer_threshold is None:
            raise Exception("Please set dealer_threshold")
        self.dealer_threshold = dealer_threshold
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.p_cross = p_cross
        self.p_mut = p_mut
        self.info()

    def info(self):
        if not self.__was_changed:
            print("INITIAL EVOLUTION SETTINGS")
        print(f"Population Size: {self.population_size}")
        print(f"Number of Generations: {self.number_of_generations}")
        print(f"Crossover Probability: {self.p_cross}")
        print(f"Mutation Probability: {self.p_mut}")
        print()

    def set(self, **kwargs):
        self.__was_changed = True
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def create_first_population(self):
        if self.population_size is None:
            raise Exception("population_size wasn't set")
        for _ in range(self.population_size):
            self.population.append(Strategy(self.dealer_threshold))

        print(f"Population with {self.population_size} individuals was created!")

    def _selection_process(self):
        # TODO: implement _selection_process()
        pass

    def _fitness_process(self):
        for strategy in self.population:
            strategy.fitness()

    def _crossover_process(self):
        # TODO: implement _crossover_process()
        pass

    def _mutation_process(self):
        # TODO: implement _mutation_process()
        pass

    def get_best(self):
        # TODO: implement get_best()
        pass

    def run_one_epoch(self):
        print(f"{'='*30+'>'} #{self.__current_epoch}")
        # EVALUATING FITNESS SCORES
        self._fitness_process()

        # PROCESS OF SELECTION
        self._selection_process()

        # PROCESS OF CROSSOVER
        self._crossover_process()

        # PROCESS OF MUTATION
        self._mutation_process()

        self.__current_epoch += 1

    def evolve(self):
        for i in range(self.number_of_generations):
            print(f"Started #{i}")
            self.run_one_epoch()
            print(f"Finished #{i}")

