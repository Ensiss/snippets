from random import random
from PIL import Image, ImageDraw
import numpy as np
import math

def get_norm_vec():
    v1 = (random() * 2 - 1, random() * 2 - 1)
    sz = math.sqrt(v1[0] * v1[0] + v1[1] * v1[1])
    return (v1[0] / sz, v1[1] / sz)

out = Image.new("RGB", (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(out)
px = out.load()
px[10, 100] = (255, 0, 0)

v1 = get_norm_vec()
v2 = get_norm_vec()
pts = []
for i in range(300):
    r1 = random() * 200 - 100
    r2 = random() * 200 - 100
    x = int(200 + r1 * v1[0] + r2 * v2[0])
    y = int(200 + r1 * v1[1] + r2 * v2[1])
    pts.append([x, y])
    px[x, y] = (255, 0, 0)

matrix = np.matrix(pts)
mean = matrix.mean(axis = 0)
for pt in matrix:
    pt -= mean
var_cov = matrix.transpose() * matrix
vals, vecs = np.linalg.eigh(var_cov)

vals, vecs = [list(x) for x in zip(*sorted(zip(vals, vecs), key=lambda pair: pair[0]))]

st = (mean[0, 0], mean[0, 1])
for i in range(2):
    ratio = vals[i] / vals[1]
    end = (st[0] + ratio * 100 * vecs[i][0, 0], st[1] + ratio * 100 * vecs[i][0, 1])
    print vals[i], vecs[i]
    draw.line((st, end), fill="#0000FF")

out.show()
