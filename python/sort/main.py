import sys
import sort
import time
import random

array = [564,123,85,48,78,6]

def genArray(size):
    array = []
    for i in range(size):
        while True:
            n = int(random.random() * 1000000000)
            if n not in array:
                array.append(n)
                break
    return array


def benchmark(name, func, tab, it):
    sys.stdout.write("%d tests with %s..." % (len(tab), name))
    sys.stdout.flush()
    t = time.clock()
    for i in range(it):
        func(tab)
    t = time.clock() - t
    print " done in %.3f s" % t

i = 10
while i < 1000000:
    a = genArray(i)
    benchmark("Bubble", sort.bubble, a, 1)
    benchmark("Insert", sort.insert, a, 1)
    benchmark("Merge", sort.merge, a, 1)
    benchmark("Quick", sort.quick, a, 1)
    i *= 10
