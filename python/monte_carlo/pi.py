from random import random as r

i, a = 0, 0.
while True:
    a += (r() ** 2 + r() ** 2 < 1)
    i += 1
    print (a / i) * 4
