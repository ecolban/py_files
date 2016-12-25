def memoize(f):
    memo = {}
    def memoized(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return memoized

def is_prime(n):
    return n == 2 or n % 2 != 0 and all(n % k != 0 for k in xrange(3, root(n) + 1, 2))

def root(p):
    return int(p ** 0.5)

@memoize
def statement1(s):
    return not(s % 2 == 0 or is_prime(s - 2))

@memoize
def statement2(p):
    return sum(statement1(i + p / i) for i in xrange(2, root(p) + 1) if p % i == 0) == 1

@memoize
def statement3(s):
    return sum(statement2(i * (s - i)) for i in xrange(2, s / 2 + 1)) == 1

def solutions(s_max):
    return [(i, s - i) for s in xrange(7, s_max + 1, 2)
                           for i in xrange(2, (s + 1) / 2) \
            if statement1(s) and statement2(i * (s - i)) and statement3(s)]

def check2(p):
    return sum(statement1(i + p / i) for i in xrange(2, root(p) + 1) if p % i == 0)
    
def check3(s):
    return [(i, s - i, check2(i * (s - i))) for i in xrange(2, s / 2 + 1)]

