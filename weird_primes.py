from fractions import gcd

g = [(5, 5), (6, 3), (11, 11), (12, 3), (23, 23), (24, 3), (47, 47), (48, 3),
          (50, 5), (51, 3), (101, 101), (102, 3), (105, 7), (110, 11), (111, 3),
          (117, 13), (233, 233), (234, 3), (467, 467), (468, 3), (470, 5),
          (471, 3), (941, 941), (942, 3), (945, 7), (1889, 1889), (1890, 3),
          (3779, 3779), (3780, 3), (7559, 7559), (7560, 3), (7566, 13),
          (15131, 15131), (15132, 3), (15158, 53), (15159, 3), (15162, 7),
          (30323, 30323), (30324, 3), (60647, 60647), (60648, 3), (60650, 5),
          (60651, 3), (60701, 101), (60702, 3), (121403, 121403), (121404, 3),
          (242807, 242807), (242808, 3), (242810, 5), (242811, 3), (242820, 19),
          (242823, 7), (242825, 5), (242826, 3), (242849, 47), (242850, 3),
          (242868, 37), (242870, 5), (242871, 3), (242879, 17), (242880, 3),
          (242979, 199), (243005, 53), (243006, 3), (243020, 29), (243021, 3),
          (486041, 486041), (486042, 3), (486045, 7), (486255, 421), (486266, 23),
          (486267, 3), (972533, 972533), (972534, 3), (972822, 577), (972825, 7),
          (1945649, 1945649), (1945650, 3), (1945731, 163)]

g_vals = map(lambda (x, y): y, g)
g_keys = map(lambda (x, y): x, g)
g_dict = {k:v for (k, v) in g}


def an_():
    n, a = 1, 7
    while True:
        yield a
        n += 1
        a += gcd(n, a)

def an(n):
    return 6 + n + sum(g_dict[i] - 1 for i in g_keys if i <= n) 


def gn_():
    yield 1
    a = an()
    t, tn = a.next(), a.next()
    while True:
        yield tn - t
        t, tn = tn, a.next()

def gn():
    n = 1
    while True:
        yield g_dict.get(n, 1)
        n += 1


def count_ones_(n):
    g = gn()
    return sum(1 if g.next() == 1 else 0 for _ in xrange(n))

def count_ones(n):
    return n - len([i for i in g_keys if i <= n])

def pn_(n):
    primes, g = set(), (t for t in gn() if t != 1)
    while len(primes) < n: primes.add(g.next())
    return primes

def pn(n):
    return sorted(set(g_vals))[:n]

def max_pn_(n):
    return max(pn(n))

def max_pn(n):
    return sorted(set(g_vals))[n]

from itertools import izip

def an_over_():
    z = enumerate(izip(an(), gn()), 1)
    return (a / i for i, (a, g) in z if g > 1)

def an_over_average_(n):
    a = an_over()
    return sum(a.next() for _ in xrange(n)) / n

def an_over_average(n):
    return 3
