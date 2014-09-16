from random import random
from PIL import Image, ImageDraw
import sys

if len(sys.argv) < 2:
    print "Usage: python dbscan.py <path_to_wallpaper>"
    exit()

def getPts(px, (w, h)):
    a = {}
    for y in range(h):
        for x in range(w):
            a[(x, y)] = 0
    return a

def dist(px, a, b):
    s = sum([(px[a][i] - px[b][i]) ** 2 for i in range(3)])
    s += sum([(a[i] - b[i]) ** 2 for i in range(2)])
    return s

def eNeighborhood(px, (w, h), (x, y), e):
    n = []
    minx, miny = (max(0, x - e), max(0, y - e))
    maxx, maxy = (min(w, x + e), min(h, y + e))
    e = (e ** 2);
    for j in xrange(miny, maxy):
        for i in xrange(minx, maxx):
            d = dist(px, (x, y), (i, j))
            if d < e:
                n.append((i, j))
    return n

def getCluster(px, sz, pts, curr, neighbors, e, clustersz):
    cluster = [curr]
    while len(neighbors):
        pt = neighbors.pop()
        if pt in pts:
            del pts[pt]
            ptneighbors = eNeighborhood(px, sz, pt, e)
            if ptneighbors >= clustersz:
                neighbors += ptneighbors
            cluster.append(pt)
    return cluster

def dbscan(px, sz, pts, e, clustersz):
    clusters = []
    while len(pts):
        key, value = pts.popitem()
        n = eNeighborhood(px, sz, key, e)
        if len(n) >= clustersz:
            clusters.append(getCluster(px, sz, pts, key, n, e, clustersz))
    return clusters

img = Image.open(sys.argv[1])
img = img.resize((200, 200), Image.ANTIALIAS)
out = Image.new("RGB", (200, 200))
px = img.load()
outpx = out.load()
pts = getPts(px, img.size)

clusters = dbscan(px, img.size, pts, 5, 20)
for c in clusters:
    avg = [0, 0, 0]
    for pt in c:
        for i in range(3):
            avg[i] += px[pt][i]
    for i in range(3):
        avg[i] /= len(c)
    for pt in c:
        outpx[pt] = tuple(avg)

img.show()
out.show()
