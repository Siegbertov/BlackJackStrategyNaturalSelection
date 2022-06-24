from .strategy import Strategy
from tqdm import tqdm


class Evolution:
    __slots__ = ('_player_threshold',  # stand = None
                 '_dealer_threshold',  # stand = 17

                 '_population_size',  # stand = 100
                 '_number_of_generations',  # stand = 10
                 '_number_of_games_for_fitness',  # stand = 1000

                 '_selection_method',  # "win" or "lose"
                 '_p_crossover',  # stand = 0.9
                 '_p_mutation',  # stand = 0.1

                 '__population',  # stand = []
                 '__current_epoch')  # stand = 0

    def __init__(self, player_threshold=None, dealer_threshold=None,
                 population_size=None, number_of_generations=None,
                 number_of_games_for_fitness=None,
                 selection_method=None, p_crossover=None, p_mutation=None):
        self.__current_epoch = 0
        self.__population = []

        self._player_threshold = player_threshold
        self._dealer_threshold = 17 if dealer_threshold is None else dealer_threshold

        self._population_size = 100 if population_size is None else population_size
        self._number_of_generations = 10 if number_of_generations is None else number_of_generations
        self._number_of_games_for_fitness = 1000 if number_of_games_for_fitness is None else number_of_games_for_fitness

        self._selection_method = "win" if selection_method is None else selection_method
        self._p_crossover = 0.9 if p_crossover is None else p_crossover
        self._p_mutation = 0.9 if p_mutation is None else p_mutation

    def load_from_file(self, name_of_file):
        # TODO implement for loading METADATA from txt file
        pass

    def show(self):
        for st in self.__population:
            print(st.fitness_score)

    def info(self):
        # TODO implement showing info of METADATA
        pass

    def set(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(f"_{key}", value)

    def create_first_population(self):
        for _ in tqdm(range(self._population_size)):
            self.__population.append(Strategy(self._player_threshold, self._dealer_threshold))
        print(f"Population with {self._population_size} individuals was created!")

    def _fitness_process(self):
        for strategy in tqdm(self.__population):
            strategy.fitness(self._number_of_games_for_fitness, self._selection_method)

    def _selection_process(self):
        # TODO: implement _selection_process()
        self.__population = sorted(self.__population, key=lambda strategy: strategy.fitness_score, reverse=(True if self._selection_method=="win" else False))

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
        print(f"{'='*30+'>'} Epoch #{self.__current_epoch}")
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
        for i in range(self._number_of_generations):
            print(f"Started #{i}")
            self.run_one_epoch()
            print(f"Finished #{i}")

