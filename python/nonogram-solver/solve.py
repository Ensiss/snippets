w = 10
h = 10
tab = [[None for i in range(w)] for i in range(h)]
vtcl = [[1, 4], [1, 1], [1, 1, 2], [6, 1], [3, 1, 3], [3, 1, 3], [2, 2], [6], [1, 1], [1, 1]]
hztl = [[3], [4], [4], [3, 1], [1, 1, 1, 1], [4, 2], [1, 1, 1, 1], [1, 1, 2, 2], [1, 1, 4, 1], [1, 2, 1]]

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

if len(vtcl) != h or len(hztl) != w:
    print "The grid size and instructions don't match"
    exit()

play()
print_tab()
