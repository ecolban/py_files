class Number(object):

    def __init__(self, n, mask):
        self._n = n
        self._mask = mask

    def __add__(self, m):
        return Number(self._n + m._n, self._mask)

    def __sub__(self, m):
        return Number(self._n - m._n, self._mask)

    def __le__(self, m):
        return self._n <= m._n

    def __lt__(self, m):
        return self._n < m._n

    def __eq__(self, m):
        return self._n == m._n

    def __ne__(self, m):
        return self._n != m._n

    def __neg__(self):
        return Number(-self._n, self.mask)

    def __lshift__(self, m):
        return Number(self._n << m._n, self._mask)

    def __rshift__(self, m):
        return Number(self._n >> m._n, self._mask)

    def __xor__(self, m):
        return Number(self._n ^ m._n, self._mask)

    def __and__(self, m):
        return Number(self._n & m._n, self._mask)

    def __or__(self, m):
        return Number(self._n | m._n, self._mask)

    def __inv__(self, m):
        return Number(~self._n, self._mask)

    def __nonzero__(self):
        return self != zero


    def to_int(self):
        return self._n ^ self._mask

    def __str__(self):
        return 'Number(%d)' % self._n


import random

mask = random.randrange(2, 1<<63) 
zero = Number(0, mask)
one = Number(1, mask)


def guarded(f):

    def _h(a, b):
        print('Guarded %s.' % str(f))
        a = Number(a, mask)
        b = Number(b, mask)
        try:
            return f(a, b).to_int() ^ mask
        except:
            raise TypeError("Your sensei frowns upon you!")

    return _h


def multiply(n, f):
    b, p = one, zero
    
    while b <= n: b <<= one
    while b > one:
        b >>= one
        p <<= one 
        if b <= n: 
            n ^= b
            p += f
    return p;


def multiply2(n, f):
    s = zero
    while n > zero:
        if n & one: s += f
        n >>= one
        f <<= one
    return s

multiply3=m=lambda x,y,o=one:y and(y&o and x)+(m(x,y>>o)<<o)

from random import randrange

a = randrange(1, 1 << 62)
b = randrange(1, 1 << 62)

guarded_multiply = guarded(multiply)


