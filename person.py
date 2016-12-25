class person(object):
    def __init__(self, born, dead):
        self.born = born
        self.dead = dead


people = []
from random import randrange

for y in range(1900, 2001):
    born = randrange(10, 21)
    for p in range(born):
        p = person(y, min(y + randrange(10, 80), 2000))
        people.append(p)

alive_diff = [0] * 101
for p in people:
    alive_diff[p.born - 1900] += 1
    alive_diff[p.dead - 1900] -= 1

max_year = 1900
max_people = 0
alive = 0
for y in range(0, 101):
    alive += alive_diff[y]
    if alive > max_people:
        max_year = 1900 + y
        max_people = alive


