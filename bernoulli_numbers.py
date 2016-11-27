from fractions import Fraction

def bernoulli(n):
    a = [Fraction(1, m + 1) for m in range(n + 1)]
    for m in range(n + 1):
        for j in range(m, 0, -1):
            a[j - 1] = Fraction(j, 1) * (a[j - 1] - a[j])
    return str(a[0])
