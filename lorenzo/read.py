from classes import *


def read(path):

    with open(path, 'r') as file:

        # example
        # npizza, n2pt, n3pt, n4pt = [int(value) for value in file.readline().rstrip().split(' ')]

        duration, n_intersec, n_streets, n_cars, bonus = [int(value) for value in file.readline().rstrip().split(' ')]

        for i in range(n_streets):

            row = file.readline().rstrip().split(' ')
            start = int(row[0])
            end = int(row[1])






        print()

    return 0
