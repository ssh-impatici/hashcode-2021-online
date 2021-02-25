import time
from math import ceil

from read import read
from write import write
from judge import judge

from classes import *

path = './data/'


def solver(task):

    start = time.time()

    duration, n_intersec, n_streets, n_cars, bonus, streets, cars, intersections = read(path + task + '.txt')

    output = []

    # TODO Scartare qualcosa
    '''
    # Eliminare strade non usate
    streets_to_delete = []
    for i, street in streets.items():
        if len(street.cars) == 0:
            streets_to_delete.append(i)

    for i in streets_to_delete:
        streets.pop(i)
    '''

    for car in cars:
        car.score = 1/(sum(street.time for street in car.streets)*len(car.streets)) # TODO

    # Ho paura sia ricorsivo,

    street_score_min = 9999999999
    street_score_max = -1
    for i, street in streets.items():
        if len(street.cars) == 0:
            street.score = 0
        else:
            street.score = sum(car.score for car in street.cars)/(street.time*len(street.cars)) # TODO

        if street_score_min > street.score:
            street_score_min = street.score
        if street_score_max < street.score:
            street_score_max = street.score

    # Schedulando
    for inter in intersections:
        bool = False
        schedule = Schedule([],inter)

        for street in inter.streets_in:
            COST_TIME = 6 # TODO
            score_norm = int(ceil(COST_TIME*(street.score - street_score_min)/(street_score_max - street_score_min))) # TODO
            if score_norm > 0:
                bool = True
                sp = SchedulePair(street, score_norm)
                schedule.pairs.append(sp)

        if bool:
            output.append(schedule)

    write('./output/' + task + '.txt', output)

    score = judge(output)

    # print(task, str(time.time() - start), str(score))
    print(task, str(time.time() - start))