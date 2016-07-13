def rotate_matrix(m):
    dim = len(m)
    if dim < 2: return m
    for i in range(dim / 2):
        for j in range((dim + 1) / 2):
            r, c = i, j
            tmp = m[r][c]
            for _ in xrange(3):
                m[r][c] = m[dim - c - 1][r]
                r, c = dim - c - 1, r
            m[r][c] = tmp

def print_matrix(m):
    dim = len(m)
    if dim < 2: print(m)
    else:
        print('[' + str(m[0]))
        for i in xrange(1, dim - 1): print(' ' + str(m[i]))
        print(' ' + str(m[dim -1]) + ']')

from decorators import memoize

@memoize
def f(eggs, drops):
    if eggs == 0 or drops == 0: return 0
    return f(eggs - 1, drops - 1) + 1 + f(eggs, drops - 1)

# num_drops =  next(d for d in xrange(100) if f(2, d) >= 100)


class EggDrop(object):

    @staticmethod
    @memoize
    def f(eggs, drops):
        if eggs == 0 or drops == 0: return 0
        return EggDrop.f(eggs - 1, drops - 1) + 1 + EggDrop.f(eggs, drops - 1)

    def __init__(self, eggs, drops):
        self._floor = randrange(1, EggDrop.f(eggs, drops) + 1)
        self._eggs = eggs
        self._drops = drops
        self._checked = False

    @property
    def floor(self):
        return "Nope"

    @property
    def __dict__(self):
        return 'Nope'

    @property
    def drops(self):
        return self._drops

    @property
    def eggs(self):
        return self._eggs

    def drop(self, n):
        if self._drops <= 0 or self._eggs <= 0:
            raise EOFError('No more drops allowed')
        self._drops -= 1
        if n >= self._floor:
            self._eggs -= 1
            return True
        else:
            return False
            

    def check(self, n):
        if self._checked:
            raise EOFError('Can only check once.')
        self._checked = True
        return n == self._floor

def simulation_egg_drop(emulator):

    @memoize
    def f(eggs, drops):
        if eggs == 0 or drops == 0: return 0
        return f(eggs - 1, drops - 1) + 1 + f(eggs, drops - 1)

    def solve(low, high, eggs, drops):
        if high < low: return low
        n = min(low + f(eggs - 1, drops - 1), high)
        if emulator.drop(n):
            print('Floor = %d, Eggs left = %d, Drops left = %d, Splat!!' % (n, eggs - 1, drops -1))
            return solve(low, n - 1, eggs - 1, drops -1)
        else:
            print('Floor = %d, Eggs left = %d, Drops left = %d' % (n, eggs, drops -1))
            return solve(n + 1, high, eggs, drops -1)
    eggs = emulator.eggs
    drops = emulator.drops
    
    return solve(1, f(eggs, drops), eggs, drops)

import abc

from random import randrange

class Child(object):

    __metaclass__ = abc.ABCMeta

    total_girls = 0
    total_boys = 0

    @classmethod
    def reset(cls):
        cls.total_girls = 0
        cls.total_boys = 0

    @classmethod
    def produce_child(cls):
        if randrange(2) == 0:
            cls.total_girls += 1
            return Girl()
        else:
            cls.total_boys += 1
            return Boy()

    @abc.abstractproperty
    def sex(self):
        pass

class Girl(Child):

    @property
    def sex(self):
        return 'F'
    

class Boy(Child):

    @property
    def sex(self):
        return 'M'

class Family(object):

    def __init__(self):
        self._num_boys = 0
        
    def make_children(self):
        has_girl = False
        while not has_girl:
            child = Child.produce_child()
            if child.sex == 'M':
                self._num_boys += 1
            else:
                has_girl = True

    def num_girls(self):
        return 1

    def num_boys(self):
        return self._num_boys


def simulation(n):
    Child.reset()
    families = [Family() for _ in xrange(n)]
    total_girls = 0
    total_boys = 0
    for f in families:
        f.make_children()
        total_girls += f.num_girls()
        total_boys += f.num_boys()
    assert total_girls == Child.total_girls
    assert total_boys == Child.total_boys
    print('Girls: %d, Boys: %d' % (total_girls, total_boys))
    

    
