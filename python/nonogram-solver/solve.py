import re
import sys

w = 0
h = 0
tab = None
vtcl = []
hztl = []

def count_none():
    c = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == None:
                c += 1
    return c

def print_tab():
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == None:
                print '  ',
            elif tab[i][j] == 0:
                print '. ',
            else:
                print '# ',
        print ''

def get_line(lx, ly):
    l = []
    dx, dy = not lx, not ly
    x, y = lx + dx - 1, ly + dy - 1
    while x < w and y < h:
        l.append(tab[y][x])
        x, y = x + dx, y + dy
    return (l)

def set_line(lx, ly, line):
    if len(line) == 0:
        return
    dx, dy = not lx, not ly
    x, y = lx + dx - 1, ly + dy - 1
    i = 0
    while x < w and y < h:
        if line[i] != None:
            tab[y][x] = line[i]
        x, y = x + dx, y + dy
        i += 1

def possibilities(lx, ly):
    def subsearch(line, out, ix, nb):
        if len(nb) == 0:
            for i in range(len(line)):
                if line[i] != None and line[i] != out[i]:
                    return
            res.append(out)
            return
        for start in range(ix, len(out)):
            cpy = out[:]
            if sum(nb) + len(nb) - 1 > len(out) - start:
                break
            for i in range(nb[0]):
                cpy[start + i] = 1
            if start + nb[0] < len(out):
                cpy[start + nb[0]] = 0
            subsearch(line, cpy, start + nb[0] + 1, nb[1:])

    line = get_line(lx, ly)
    nb = hztl[lx - 1] if lx else vtcl[ly - 1]
    res = []
    subsearch(line, [0] * len(line), 0, nb)
    if len(res) == 0:
        return []
    sums = [sum([res[i][j] for i in range(len(res))]) for j in range(len(res[0]))]
    return [0 if not i else 1 if i == len(res) else None for i in sums]

def play():
    c = oldc = count_none()
    while c:
        for x in range(1, w + 1):
            set_line(x, 0, possibilities(x, 0))
        for y in range(1, h + 1):
            set_line(0, y, possibilities(0, y))
        c = count_none()
        if c == oldc:
            print "Error: I can't solve this grid"
            exit()
        oldc = c

def check_valid():
    def check_line(x, y, l):
        l = [len(i) for i in re.sub("\.+", " ", "".join([".#"[i] for i in l])).split()]
        if len(l) == 0:
            l.append(0)
        nb = hztl[x - 1] if x else vtcl[y - 1]
        if l != nb:
            print "Error: ",
            print "horizontal #" + str(x) if x else "vertical #" + str(y),
            print " seems to be wrong"
            exit()

    for x in range(1, w + 1):
        check_line(x, 0, get_line(x, 0))
    for y in range(1, h + 1):
        check_line(0, y, get_line(0, y))

def load_grid(silent = False):
    global tab, w, h, vtcl, hztl

    def get_values(msg):
        while True:
            if not silent: print msg,
            try:
                inp = [int(i) for i in raw_input().split(" ")]
            except:
                print "Wrong input format"
                continue
            if len(inp) == 0:
                print "Not enough arguments"
                continue
            return inp

    while w == 0 or h == 0:
        inp = get_values("Grid size (width height):")
        if len(inp) != 2:
            print "Wrong number of arguments"
            continue
        w, h = inp
    tab = [[None for i in range(w)] for i in range(h)]
    if not silent: print "Enter vertical instructions (one row per line, values separated by spaces) :"
    for i in range(h):
        vtcl.append(get_values("Row #" + str(i + 1) + ":"))
    if not silent: print "Enter horizontal instructions (one column per line, values separated by spaces) :"
    for i in range(w):
        hztl.append(get_values("Column #" + str(i + 1) + ":"))
    if len(vtcl) != h or len(hztl) != w:
        # Should not happen
        print "The grid size and instructions don't match"
        exit()

if "-h" in sys.argv:
    print "Usage: " + sys.argv[0] + " OPTIONS"
    print "\t-h: display this help and exit"
    print "\t-s: silent, don't prompt for user input (useful for scripts)"
    exit()

load_grid("-s" in sys.argv)
play()
check_valid()
print_tab()
