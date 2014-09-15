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

if len(sys.argv) < 2:
    print "Usage: python looknsay.py <iterations> [seed]"
    exit()
print lookNsay("1" if len(sys.argv) < 3 else sys.argv[2], int(sys.argv[1]))
