def matches(i, j):
    return i * j % 101 == 1


def find_pairs(a_set):
    res = set()
    s = a_set.copy()
    while s:
        x = s.pop()
        y = next(y for y in s if matches(x, y))
        res.add((x, y))
        s.remove(y)
    return res

a = set(range(2, 100))

b = find_pairs(a)




