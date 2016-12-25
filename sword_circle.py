def sword_circle_rec(n):

    def f(n, s, p, q):
        print('n = %d, s = %d, p = %d, q = %d' % (n, s, p, q))
        if n <= 2: return q
        s = (n + s) % 2
        p <<= 1
        return f((n + s) // 2, s, p, q + s * p)

    return f(n, 0, 1, 0) + 1

def sword_circle(n):
    s, p, q = 0, 1, 0
    while n > 2:
        s = (n + s) % 2
        n = (n + s) // 2
        p <<= 1
        q += s * p
    return q + 1

def sword_circle_2_rec(n, k):

    def f(n, k):
        if n == 1: return 0
        return (f(n - 1, k) + k) % n

    return f(n, k) + 1

def sc(n):
    res = 0
    for i in xrange(2, n + 1):
        res = (res + 2) % i
    return res + 1



