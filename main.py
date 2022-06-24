from natural_selection import Evolution


def main():
    my_evolution = Evolution()
    my_evolution.set(number_of_games_for_fitness=2000, selection_method='lose')
    my_evolution.create_first_population()
    my_evolution._fitness_process()
    my_evolution._selection_process()
    my_evolution.show()

if __name__ == "__main__":
    main()
