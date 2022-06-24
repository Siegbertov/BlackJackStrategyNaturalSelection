from natural_selection import Evolution


def main():
    my_evolution = Evolution(dealer_threshold=16, population_size=100)
    # my_evolution.set(population_size=100)
    # my_evolution.set(number_of_generations=10)
    # my_evolution.set(p_cross=10)
    # my_evolution.set(p_mut=10)
    # my_evolution.info()
    my_evolution.create_first_population()


if __name__ == "__main__":
    main()
