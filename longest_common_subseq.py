from decorators import memoize
from immutable import EmptyList

def longest_common_subseq_1(a, b):

    @memoize
    def h(i, j):
        if i == 0 or j == 0: return ''
        return h(i-1, j-1) + a[i-1] if a[i-1]==b[j-1] \
               else max(h(i-1, j), h(i, j-1), key=len)

    return h(len(a), len(b))

def longest_common_subseq(a, b):

    e = EmptyList()
    v = [e] * (len(b) + 1)

    for c in a:
        ul = e
        for j in xrange(1, len(b)+1):
            ul, v[j] = v[j], ul.cons(c) if c == b[j-1] else max(v[j], v[j-1], key=len)
        
    return ''.join(v[len(b)].reverse())
