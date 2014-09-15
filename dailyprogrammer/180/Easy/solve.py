from itertools import groupby

r = "1"
for i in range(int(__import__("sys").argv[1])):
    r = "".join([str(len(s)) + s[0] for s in ["".join(s) for k, s in groupby(r)]])
print r
