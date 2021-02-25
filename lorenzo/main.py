from multiprocessing import Process

from solver import solver

if __name__ == '__main__':

    tasks = [
        'a_example'
    ]

    for task in tasks:
        process = Process(target=solver, args=([task]))
        process.start()