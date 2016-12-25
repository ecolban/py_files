from heapq import heappop, heappush

def dbl_linear(n):
    heap, last = [1], -1
    for n in xrange(n + 1):
        e = heappop(heap)
        while e == last: e = heappop(heap)
        last = e
        heappush(heap, 2 * e + 1)
        heappush(heap, 3 * e + 1)
    return last

def is_dbl_lin(n):
    if n < 1: return False
    if n == 1: return True
    return (n - 1) % 2 == 0 and is_dbl_lin(n / 2) or\
        (n - 1) % 3 == 0 and is_dbl_lin(n / 3)

def dbl_lin_gen():
    yield(1)
    n = 2
    while True:
        while not is_dbl_lin(n): n += 1
        yield(n)
        n += 1

def dbl_linear2(n):
    lg = dbl_lin_gen()
    for i in xrange(n): lg.next()
    return lg.next()

                                           
