from natural_selection import Evolution


def main():
    my_evolution = Evolution()
    my_evolution.set(number_of_games_for_fitness=2000, selection_method='win', number_of_generations=6)
    my_evolution.create_first_population()
    my_evolution.evolve()


if __name__ == "__main__":
    main()
