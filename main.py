# from natural_selection import Evolution
#
#
# my_evolution = Evolution()
#
#
# my_evolution.evolve()


def main():
    cards = ('A', '10', '9', '8', '7', '6', '5', '4', '3', '2')
    inputs = tuple([f"{c1}_{c2}_{c3}" for c1 in cards for c2 in cards[cards.index(c1):] for c3 in cards])
    print(len(inputs))


if __name__ == "__main__":
    main()
