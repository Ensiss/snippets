import random

def bubble(l):
    ret = l[:]
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if ret[j] > ret[j + 1]:
                ret[j], ret[j + 1] = ret[j + 1], ret[j]
    return (ret)

def insert(l):
    ret = []
    for i in range(0, len(l)):
        for j in range(0, i + 1):
            if j == i or l[i] < ret[j]:
                ret.insert(j, l[i])
                break
    return (ret)

def merge(l):
    if len(l) == 1:
        return l
    a = merge(l[:len(l) / 2])
    b = merge(l[len(l) / 2:])
    ret = []
    while a or b:
        ret.append([b, a][a and b and a[0] < b[0] or not b].pop(0))
    return ret

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
            l[a], l[b] = l[b], l[a]
        _qsub(l, idx, a - idx)
        _qsub(l, a + 1, idx + sz - a - 1)
        return l
    return _qsub(l[:], 0, len(l))
