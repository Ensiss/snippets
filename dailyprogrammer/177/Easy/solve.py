import random
import sys

def _swap(array, a, b):
    buf = array[a]
    array[a] = array[b]
    array[b] = buf

def quick(l):
    def _qsub(l, idx, sz):
        if sz < 2:
            return l
        pivot = l[idx + int(random.random() * sz)]
        a = idx
        b = idx + sz - 1
        while a < b:
            while l[a] < pivot:
                a += 1
            while l[b] > pivot:
                b -= 1
            _swap(l, a, b)
        _qsub(l, idx, a - idx)
        _qsub(l, a + 1, idx + sz - a - 1)
        return l
    return _qsub(l[:], 0, len(l))

print quick([int(x) for x in sys.argv[1:]])
