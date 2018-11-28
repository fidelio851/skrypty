#!/usr/bin/python

import random
from multiprocessing import Pool
import multiprocessing as mp
from multiprocessing import Process
from multiprocessing import Lock, Array



random.seed(123)

# Define an output queue
output = mp.Queue()

# define a example function
def rand_list(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_list = []
    for i in range(0,100):
        rand_list.append(random.randint(0, 39))
    output.put(rand_list)

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_list, args=(5, output)) for x in range(4)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)