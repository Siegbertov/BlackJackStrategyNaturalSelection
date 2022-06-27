from natural_selection import Evolution


def main():
    my_evolution = Evolution()
    my_evolution.set(number_of_games_for_fitness=2000)
    my_evolution.set(selection_method='lose')
    # my_evolution.set(number_of_generations=10)
    my_evolution.set(fitness_goal=0.49)
    my_evolution.init()
    my_evolution.evolve()


if __name__ == "__main__":
    main()
