import sys

if len(sys.argv) < 5:
    print "Usage: ./solve.py text <col_nb> <col_width> <space_width>"
    exit()

nb, w, spw = [int(i) for i in sys.argv[2:]]
txt = "".join([l.strip() for l in open(sys.argv[1])])
lines = (len(txt) / w) / nb
cols = []

for i in range(nb):
    cols.append([])
    for l in range(lines):
        cols[-1].append(txt[:w])
        txt = txt[w:]

for l in range(lines):
    print (" " * spw).join([cols[i][l] for i in range(nb)])
