from classes import *


def read(path):
    with open(path, 'r') as file:

        # example
        # npizza, n2pt, n3pt, n4pt = [int(value) for value in file.readline().rstrip().split(' ')]

        streets = []
        cars = []

        intersections = []

        duration, n_intersec, n_streets, n_cars, bonus = [int(value) for value in file.readline().rstrip().split(' ')]

        intersections = [Intersection(i, 0, 0) for i in range(n_intersec)]

        for i in range(n_streets):
            row = file.readline().rstrip().split(' ')
            int_in = int(row[0])
            int_out = int(row[1])
            name = row[2]
            duration = int(row[3])

            streets.append(Street(name, int_in, int_out, duration))

            intersections[int_in].streets_out += 1
            intersections[int_out].streets_in += 1

        for i in range(n_cars):
            cars.append(Car(file.readline().rstrip().split(' ')[1:]))

    return duration, n_intersec, n_streets, n_cars, bonus, streets, cars, intersections
