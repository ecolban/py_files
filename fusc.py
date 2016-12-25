def memoize(f):
    memo = {}
    def h(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return h

@memoize
def fusc_rec(n):
    if n <= 1: return n
    elif n % 2 == 0: return fusc(n / 2)
    else: return fusc(n/2) + fusc(n/2 + 1)


def fusc_tailrec(n):
    def f(a, b, n):
        if n == 1: return a + b
        elif n % 2 == 0: return f(a + b, b, n / 2)
        else: return f(a, a + b, n / 2)
    return 0 if n == 0 else f(1, 0, n)


def fusc(n):
    a, b = 1, 0
    while n > 0:
        if n % 2 == 1: b += a
        else: a += b
        n >>= 1
    return b

def fusc_alt(n):
    d, a, b = 1, 1, 0
    while d <= n: d <<= 1
    while d > 1:
        d >>= 1
        if n >= d:
            n -= d
            b += a
        else:
            a += b
    return b

def fusc_alt2(n):
    a, b = 1, 0
    for i in bin(n)[2:]:
        if i == '1': b += a
        else: a += b
    return b


def fibfusc_rec(n):
    if n == 0: return (1, 0)
    (x, y) = fibfusc_rec(n >> 1)
    if n & 1 == 0: return ((x + y) * (x - y), y * (((x + y) << 1) + y))
    return (-y * (((x + y) << 1) + y), (x + (y << 1)) * (x + (y << 2)))

def fastfib(n):
    x, y = fibfusc_rec((n + 1) / 2)
    return x + y if n % 2 == 1 else y

def fibfusc(n, num_digits=None):
    if num_digits: mod = pow(10, num_digits)
    x, y = 1, 0
    for c in bin(n)[2:]:
        if c == '0': x, y = (x + y) * (x - y), y * (((x + y) << 1) + y)
        else: x, y = -y * (((x + y) << 1) + y), (x + (y << 1)) * (x + (y << 2))
        if num_digits: x, y = x % -mod, y % mod
    return x, y



 










    
