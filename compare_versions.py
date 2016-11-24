def compare(a, b):
    z = zip_longest(map(int, a.split('.')), map(int, b.split('.')), fillvalue=0)
    return next((-1 if x < y else 1 for (x, y) in z if x != y), 0)


