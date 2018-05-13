import sys
from array import array
from pprint import pprint
from random import random, randint

from matplotlib import pyplot
from numpy import average


def show(arr):
    # pprint(arr)
    pprint(average(arr))
    pprint(sum(arr))
    pyplot.plot(arr)
    pyplot.axis([1, len(arr) + 1, 0, 1])
    pyplot.show()


def print_progress(i):
    if i % 10000 == 0:
        sys.stdout.write(".")
        sys.stdout.flush()


def run_experiment(rand_strategy, input_size=1000, sample_size=10, iterations=1):
    i = 0
    inputs = [x for x in range(0, input_size)]
    stats = array('i', [0] * input_size)
    while i < iterations:
        sample = reservoir_sampling(rand_strategy, inputs, sample_size)
        for item in sample:
            stats[item] = stats[item] + 1
        i += 1
        print_progress(i)
    sys.stdout.write("\n")
    stats = list(map(lambda stat: stat / iterations, stats))
    return stats


def reservoir_sampling(rand_strategy, inputs, sample_size):
    k = sample_size
    s = inputs
    r = s[0:k]  # reservoir
    reservoir = r
    for i in range(k, len(s)):
        j = rand_strategy(i)
        if j < k:
            r[j] = s[i]
    return list(reservoir)


def main():
    # sample = reservoir_sampling([x for x in range(0, 1000)], 10)
    # pprint(sample)
    input_size = 100
    sample_size = 10
    num_iterations = 1000000
    results2 = run_experiment(lambda i: int(random() * i), input_size, sample_size, num_iterations)
    show(results2)
    results1 = run_experiment(lambda i: randint(0, i), input_size, sample_size, num_iterations)
    show(results1)


if __name__ == '__main__':
    main()
