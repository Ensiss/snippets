import sys

if len(sys.argv) < 2:
    print "Usage: %s '1+2+3...'" % sys.argv[0]
    exit()

nbs = sys.argv[1].split("+")
sz = max(map(len, nbs)) + 1
nbs = ["%0*d" % (sz, int(x)) for x in nbs]
carry = "0"
res = ""

for i in range(sz):
    s = sum([int(s[-i-1]) for s in nbs]) + int(carry[0])
    carry = str(s / 10) + carry
    res = str(s % 10) + res

print "%*d" % (sz + 1, int(carry))
print "-" * (sz + 1)
print " " + "\n+".join(["%*d" % (sz, int(s)) for s in nbs])
print "-" * (sz + 1)
print "%*d" % (sz + 1, int(res))
