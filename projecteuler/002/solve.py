def fib():
    a = b = 1
    while True:
        yield b
        tmp = b
        b += a
        a = tmp

f = fib()
s = 0
while True:
    n = f.next()
    if n >= 4000000:
        break
    elif n % 2 == 0:
        print n
        s += n
print s
