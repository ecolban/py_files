def prime_factors(n):
    if n < 2: return '(%d, 1)' % n
    if n == 2: return '(2, 1)'
    p = 2
    e = 0
    res = ''
    while p * p <= n:
        if n % p == 0:
            e += 1
            n /= p
        else:
            if e > 0: res += '(%d, %d)' % (p, e) if e > 1 else '(%d, 1)' % p
            e = 0
            p += 1 if p == 2 else 2
            
    if n == p:
        res += '(%d, %d)' % (p, e + 1)
    elif e > 1:
        res += '(%d, %d)(n, 1)' % (p, e, n)
    elif e > 0:
        res += '(%d, 1)(%d, 1)' % (p, n)
    else:
        res += '(%d, 1)' % n

    return res
