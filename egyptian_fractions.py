from fractions import Fraction

def decompose_rec(s):
    f = Fraction(s)

    def decomp(lst, n, d):
        if n == 0: return lst
        if n >= d:
            q, r = divmod(n, d)
            lst.append('%d' % q)
            return  decomp(lst, r, d)
        q, r = divmod(d, n)
        if r == 0:
            lst.append('1/%d' % q)
            return lst
        q, r = q + 1, n - r
        lst.append('1/%d' % q)
        return decomp(lst, r, d * q)

    return decomp([], f.numerator, f.denominator)

def decompose(s):
    f = Fraction(s)
    n, d = f.numerator, f.denominator
    q, n = divmod(n, d)
    res = [str(q)] if q > 0 else []
    while n > 0:
        q, r = divmod(d, n)
        if r > 0:
            q += 1
            n, d = n - r, d * q
        else:
            n = 0
        res.append('1/%d' % q)
    return ' + '.join(res) if res else '0'

                      
    
