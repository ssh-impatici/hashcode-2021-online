import time

from read import read
from write import write
from judge import judge

from classes import *

path = './data/'


def solver(task):

    start = time.time()

    duration, n_intersec, n_streets, n_cars, bonus, streets, cars, intersections = read(path + task + '.txt')

    output = []

    for intersec in intersections:
        intersec_streets = intersec.streets_in
        intersec_streets.sort(key=lambda x: x.cars, reverse=True)

        schedule_pairs = [SchedulePair(street_in, 1) for street_in in intersec_streets]
        output.append(Schedule(schedule_pairs, intersec))

    write('./output/' + task + '.txt', output)

    # score = judge(output)

    print(task, str(time.time() - start))
