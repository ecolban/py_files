from strmath import zero, one

def powmod(base, exp, mod):

    def multmod(m, n, mod):
        b = one
        p = zero
        while b <= n: b <<= one
        while b > one:
            b >>= one
            p <<= one
            if p >= mod: p -= mod
            if n >= b:
                n -= b
                p += m
                if p >= mod: p -= mod
        return p

    base = base % mod
    b = one
    p = one
    while b <= exp: b <<= one
    while b > one:
        b >>= one
        p = multmod(p, p, mod)
        if exp >= b:
            exp -= b
            p = multmod(p, base, mod)
    return p
