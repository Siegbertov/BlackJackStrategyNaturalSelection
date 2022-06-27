from .strategy import Strategy
from tqdm import tqdm


class Evolution:
    __slots__ = ('_player_threshold',  # stand = None
                 '_dealer_threshold',  # stand = 17

                 '_population_size',  # stand = 100
                 '_number_of_generations',  # stand = 10
                 '_fitness_goal',  # stand = None
                 '_number_of_games_for_fitness',  # stand = 1000

                 '_selection_method',  # "win" or "lose"
                 '_p_crossover',  # stand = 0.9
                 '_p_mutation',  # stand = 0.05

                 '__ancestors',  # stand = []
                 '__descendants',  # stand = []
                 '__current_best_strategy', # stand = None
                 '__current_generation_number')  # stand = 0

    def __init__(self, player_threshold=None, dealer_threshold=None,
                 population_size=None, number_of_generations=None,
                 number_of_games_for_fitness=None,
                 selection_method=None, p_crossover=None, p_mutation=None):
        self.__current_best_strategy = None
        self._fitness_goal = None
        self.__current_generation_number = 0
        self.__ancestors = []
        self.__descendants = []

        self._player_threshold = player_threshold
        self._dealer_threshold = 17 if dealer_threshold is None else dealer_threshold

        self._population_size = 100 if population_size is None else population_size
        self._number_of_generations = 10 if number_of_generations is None else number_of_generations
        self._number_of_games_for_fitness = 1000 if number_of_games_for_fitness is None else number_of_games_for_fitness

        self._selection_method = "win" if selection_method is None else selection_method
        self._p_crossover = 0.9 if p_crossover is None else p_crossover
        self._p_mutation = 0.05 if p_mutation is None else p_mutation

    def load_from_file(self, name_of_file):
        # TODO implement for loading METADATA from txt file
        pass

    def visualise_graph(self):
        # TODO visualizing of how __current_best_fitness_score grow through each generation
        pass

    def show(self, group="ancestors"):
        if group == "ancestors":
            print("ANCESTORS:")
            if len(self.__ancestors):
                for strategy in self.__ancestors:
                    print(strategy.fitness_score)
            else:
                print("\t<EMPTY>")
        elif group == "descendants":
            print("DESCENDANTS:")
            if len(self.__descendants):
                for strategy in self.__descendants:
                    print(strategy.fitness_score)
            else:
                print("\t<EMPTY>")
        print()

    def info(self):
        # TODO implement showing METADATA of self
        pass

    def set(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'fitness_goal':
                self.__setattr__('_number_of_generations', None)
            if key == 'number_of_generations':
                self.__setattr__('_fitness_goal', None)
            self.__setattr__(f"_{key}", value)

    def init(self):
        for _ in range(self._population_size):
            self.__descendants.append(Strategy(self._player_threshold, self._dealer_threshold))
        print(f"INITIAL POPULATION WAS CREATED!\nN={self._population_size}\n")

    def _fitness_process(self):
        for strategy in tqdm(self.__descendants, desc=f"GENERATION #{self.__current_generation_number}", unit="strategies", ncols=100):
            strategy.fitness(self._number_of_games_for_fitness, self._selection_method)
        self._move_from_desc_to_anc()
        self._sort_anc_by_fitness_score()

    def _move_from_desc_to_anc(self):
        while len(self.__descendants):
            self.__ancestors.append(self.__descendants.pop())

    def _sort_anc_by_fitness_score(self):
        self.__ancestors = sorted(self.__ancestors, key=lambda strategy: strategy.fitness_score,
                                  reverse=(True if self._selection_method == "win" else False))

    def _selection_process(self):
        while len(self.__ancestors) > 10:
            self.__ancestors.pop()

    def _crossover_process(self):
        for i, strategy_1 in enumerate(self.__ancestors):
            for j, strategy_2 in enumerate(self.__ancestors[self.__ancestors.index(strategy_1):]):
                if strategy_1 is not strategy_2:
                    new_strategy_1, new_strategy_2 = Strategy.crossover(strategy_1, strategy_2, self._p_crossover)
                    self.__descendants.append(new_strategy_1)
                    self.__descendants.append(new_strategy_2)

    def _mutation_process(self):
        for strategy in self.__descendants:
            strategy.mutate(self._p_mutation)

    def _update_best(self):
        self.__current_best_strategy = self.__ancestors[0]

    def run_one_epoch(self):
        # EVALUATING FITNESS SCORES
        self._fitness_process()

        # PROCESS OF SELECTION
        self._selection_process()

        # PROCESS OF CROSSOVER
        self._crossover_process()

        # PROCESS OF MUTATION
        self._mutation_process()

        self._update_best()
        print(f"{'=' * 30 + '>'} Generation #{self.__current_generation_number} finished")
        print(f"{'=' * 30 + '>'} Best {self._selection_method}-rate: {self.__current_best_strategy.fitness_score}")
        print()
        self.__current_generation_number += 1

    def evolve(self):
        if self._fitness_goal is None:
            for i in range(self._number_of_generations + 1):
                self.run_one_epoch()
        elif self._number_of_generations is None:
            if self.__current_generation_number == 0:
                self.run_one_epoch()
            if self._selection_method == "win":
                while self.__current_best_strategy.fitness_score < self._fitness_goal or self.__current_best_strategy is None:
                    self.run_one_epoch()
            elif self._selection_method == "lose":
                while self.__current_best_strategy.fitness_score > self._fitness_goal or self.__current_best_strategy is None:
                    self.run_one_epoch()
