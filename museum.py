
def memoize(f):
    memo = {}
    def memoized(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return memoized


def least_bribes(bribes):

    @memoize
    def f(i, j):
        assert i <= j
        if i == j: return 0
        if i + 1 == j: return bribes[i]
        return min(max(f(i, k),f(k + 1, j)) + bribes[k] for k in xrange(i, j))

    return f(0, len(bribes))

print(least_bribes(xrange(1, 21)))

from random import randrange

print(least_bribes([randrange(1, 100) for _ in xrange(100)]))

from math import exp

def ex_euler(n):
    h = 1.0 / n
    
    def f(t, y): return 2.0 - exp(-4 * t) - 2 * y
    
    X = [h * k for k in xrange(n + 1)]
    Y = [1.0] * (n + 1)
    Z = [1.0] * (n + 1)
    for k in xrange(0, n):
        Y[k + 1] = Y[k] + f(X[k], Y[k]) * h
        t = X[k + 1]
        Z[k + 1] = 1.0 + 0.5 * exp(-4.0 * t) - 0.5 * exp(-2.0 * t)
    print('X = %s\nY = %s\nZ = %s' % (X, Y, Z))
    return round(sum(abs(Y[k] - Z[k]) for k in xrange(n + 1)), 6)


def npv(c, r):
    if len(c) == 0: return 0
    return c[0] + npv(c[1:], r) / (1 + r)

def irr(c):
    print c
    
    def f(c, r):
        if len(c) == 0: return 0
        return c[0] + f(c[1:], r) / (1 + r)

    def f_prime(c, r):
        return -f(c[1:], r) / (1 + r)**2

    e = 0.000001
    r_i, r_j = 0.0, 0.5
    while abs(r_j - r_i) > e:
        print('r_j = %0.6f, npv = %0.6f' % (r_j, npv(c, r_j))) 
        r_i, r_j = r_j, r_j - f(c, r_j) / f_prime(c, r_j)
    return round(r_j, 6)


a = {'a':
     {'a':
      {'a':
       {'a': {'a': {'n': 2, 'op': 'imm'}, 'b': {'n': 3, 'op': 'imm'}, 'op': '*'},
        'b': {'n': 0, 'op': 'arg'}, 'op': '*'},
       'b': {'a': {'n': 5, 'op': 'imm'}, 'b': {'n': 1, 'op': 'arg'}, 'op': '*'}, 'op': '+'},
      'b': {'a': {'n': 3, 'op': 'imm'}, 'b': {'n': 2, 'op': 'arg'}, 'op': '*'}, 'op': '-'},
     'b': {'a': {'a': {'n': 1, 'op': 'imm'}, 'b': {'n': 3, 'op': 'imm'}, 'op': '+'},
           'b': {'a': {'n': 2, 'op': 'imm'}, 'b': {'n': 2, 'op': 'imm'}, 'op': '*'}, 'op': '+'},
     'op': '/'}
