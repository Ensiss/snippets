import re

def read_eq():
    rx = re.match("y=([-+]?[0-9]+(?:\.[0-9]+)?)?x([-+][0-9]+(?:\.[0-9]+)?)?", raw_input())
    if not rx:
        print "Input must be like: 'y=[a]x[-+][b]'"
        exit()
    gp = rx.groups()
    return float(gp[0] if gp[0] else 1), float(gp[1] if gp[1] else 0)

a, b = read_eq()
c, d = read_eq()
x = (d - b) / (a - c)
y = a * x + b
print (x, y)
