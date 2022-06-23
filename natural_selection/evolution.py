from .strategy import Strategy


class Evolution:
    def __init__(self, population_size=100, number_of_generations=10):
        self.population = []

        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.current_epoch = 0

        self.p_cross = None
        self.p_mut = None

        self._create_new_population()

    def _create_new_population(self):
        for _ in range(self.population_size):
            self.population.append(Strategy())

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
        print(f"{'='*30+'>'} #{self.current_epoch}")
        # EVALUATING FITNESS SCORES
        self._fitness_process()

        # PROCESS OF SELECTION
        self._selection_process()

        # PROCESS OF CROSSOVER
        self._crossover_process()

        # PROCESS OF MUTATION
        self._mutation_process()

        self.current_epoch += 1

    def evolve(self):
        for i in range(self.number_of_generations):
            print(f"Started #{i}")
            self.run_one_epoch()
            print(f"Finished #{i}")

