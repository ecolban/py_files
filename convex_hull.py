def hull_method(pointlist):

    def turn(p1, p2, p3):
        return (p3[1] - p1[1]) * (p2[0] - p1[0]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

    def exterior(points, direction):
        res = []
        for p in points:
            while len(res) >= 2 and direction * turn(res[-2], res[-1], p) <= 0:
                res.pop()
            res.append(p)
        return res
    
    pointlist.sort()
    start, end = pointlist[0], pointlist[-1]
    above = [p for p in pointlist if turn(start, p, end) >= 0]
    below = [p for p in pointlist if turn(start, p, end) <= 0]
    return exterior(above, 1)[:-1] + exterior(below, -1)[:0:-1]

def merge(l1, l2):
    res = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    return res + l1[i:] + l2[j:]

from math import sqrt
def distance(lst):
    def norm(u, v): return (sqrt(u * u + v * v))
    (x, y), d = lst[0], 0
    for (a, b) in lst[1:]:
        d += norm(a - x, b - y)
        x, y = a, b
    return d



from random import randrange

points = [(randrange(1000), randrange(1000)) for _ in xrange(100000)]
print(len(points))
points = [(i, j) for (i, j) in points if (i - 500) ** 2 + (j - 500) ** 2 <= 250000]
print(len(points) * 4)

hull =  hull_method(points)
print('%.2f' % distance(hull))
