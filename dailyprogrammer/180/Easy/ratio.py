import sys

def lookNsay(s, n):
    if n <= 0:
        return s
    nstr = ""
    count = 0
    prev = "\0"
    for c in s:
        if c != prev and count:
            nstr += str(count) + prev
            count = 0
        count += 1
        prev = c
    nstr += str(count) + prev
    return (lookNsay(nstr, n - 1))

s = "1"
ratio = 0
# print s
for i in xrange(100000000):
    olen = len(s)
    s = lookNsay(s, 1)
    ratio += len(s) / float (olen)
    print i + 1, ratio / (i + 1.)
