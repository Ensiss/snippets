print sum((not x % 3 or not x % 5) * x for x in xrange(1000))
