import random

def random_ints(n, total):
    arr = []
    while n > 1:
        x = random.randrange(total)
        arr.append(x)
        total -= x
        n -= 1
    return arr + [total]

def test():
    sums = [0 for _ in range(10)]
    for _ in range(10000):
        a = random_ints(10, 100)
        for i in range(10):
            sums[i] += a[i]
    print([sums[i] / 10000 for i in range(10)])

def random_ints_2(n, total):
    a = set()
    while len(a) < n - 1: a.add(random.randrange(1, total))
    a = sorted(a)
    a.append(total)
    res, last = [], 0
    for i in range(n):
        res.append(a[i] - last)
        last = a[i]
    return res
