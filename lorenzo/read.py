from classes import *


def read(path):

    with open(path, 'r') as file:

        streets = []
        cars = []
        cars_dict = {}

        duration, n_intersec, n_streets, n_cars, bonus = [int(value) for value in file.readline().rstrip().split(' ')]

        intersections = [Intersection(i, [], []) for i in range(n_intersec)]

        for i in range(n_streets):
            row = file.readline().rstrip().split(' ')
            int_in = int(row[0])
            int_out = int(row[1])
            name = row[2]
            duration = int(row[3])

            street = Street(name, int_in, int_out, duration)
            streets.append(street)

            intersections[int_in].streets_out.append(street)
            intersections[int_out].streets_in.append(street)

            cars_dict[name] = 0

        for i in range(n_cars):
            car_streets = file.readline().rstrip().split(' ')[1:]
            car = Car(car_streets)
            cars.append(car)

            for c in car_streets:
                cars_dict[c] = cars_dict[c] + 1

        for street in streets:
            street.cars = cars_dict[street.name]

    return duration, n_intersec, n_streets, n_cars, bonus, streets, cars, intersections
