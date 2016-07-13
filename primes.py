from random import randrange


def prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
              43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    if n in primes: return True
    if n < 2 or any(n % p == 0 for p in primes): return False
    if n < 10000: return True
    return rabin_miller(n)


def rabin_miller(n):
    d, s = n - 1, 0
    while d & 1 == 0:
        d >>= 1
        s += 1

    def witness(w):
        return not (pow(w, d, n) == 1 or any(pow(w, d << r, n ) == n - 1 for r in range(s)))

##    def witness(w):
##        a = pow(w, d, n)
##        if a == 1 or a == n - 1: return False
##        for _ in range(1, s):
##            a = a * a % n
##            if a == n - 1: return False
##        return True

    return not any(witness(randrange(2, n)) for _ in range(10))

def modinv(n, m):
    x, y, k = 0, 1, m
    while n > 0:
        q, r = divmod(k, n)
        x, y, k, n = y, x - q * y, n, r
    if k > 1: return None
    return m + x if x < 0 else x


def factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            res.append(k)
            n //= k
        else:
            k += 2
    if n > 1: res.append(n)
    return res






