from itertools import groupby
import sys

r = "1" if len(sys.argv) < 3 else sys.argv[2]
for i in range(5 if len(sys.argv) < 2 else int(sys.argv[1])):
    r = "".join([str(len(s)) + s[0] for s in ["".join(s) for k, s in groupby(r)]])
print r
