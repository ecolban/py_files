def quora(a):
    n = int_sqrt(len(a))
    r, c = 0, 0
    m = n * (n - 1)
    assert m + n == len(a)
    b = [[0] * n for _ in xrange(n)]
    for i in xrange(len(a)):
        r, c = divmod(i, n)
        s = r + c
        if s < n:
            b[r][c] = a[s * (s + 1) / 2 + c]
        else:
            s_1 = 2 * (n - 1) - s
            b[r][c] = a[m - s_1 * (s_1 + 1) / 2 + c]
    return b
        

def int_sqrt(n):
    b = 1 << (n.bit_length() + 1) / 2
    c = n / b
    while b - c > 1:
        b = (b + c) >> 1
        c = n / b
    return min(b, c)
