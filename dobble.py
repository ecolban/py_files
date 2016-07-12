#!/usr/bin/python

p = 7
nums = range(p)
points = [(x, y) for x in nums for y in nums]
dirs = [(1, v) for v in nums] + [(0, 1)]
lines = [(a, b, c) for (a,b) in dirs for c in nums]
line_num = {line:n for n, line in enumerate(lines, 1)}
dobble = [tuple(line_num[(a, b, (a * x + b * y) % p)] for (a, b) in dirs) for (x, y) in points]
dobble.extend(tuple(line_num[(a, b, c)] for c in nums) + (len(lines) + 1,) for (a, b) in dirs)

def mkstr(iterable, sep, start='', end=''):
    return '%s%s%s' % (start, sep.join(map(str, iterable)), end)

for t in dobble:
    print(mkstr(map(lambda n: '%02d' % n, t), ', ', start='[', end =']'))

