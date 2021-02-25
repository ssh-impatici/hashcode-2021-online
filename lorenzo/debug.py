import time

from read import read

path = './data/'

task = 'a'

start = time.time()

duration, n_intersec, n_streets, n_cars, bonus, streets, cars, intersections = read(path + task + '.txt')

output = []

# ...

# write('./output/' + task + '.txt', output)

# score = judge(output)

# print(task, str(time.time() - start), str(score))
print(task, str(time.time() - start))

