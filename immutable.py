import abc

class ImmutableList(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def head(self):
        pass

    @abc.abstractproperty
    def tail(self):
        pass

    @abc.abstractproperty
    def is_empty(self):
        pass

    @abc.abstractmethod
    def __iter__(self):
        pass

    @abc.abstractmethod
    def reverse(self):
        pass

    @abc.abstractmethod
    def __getitem__(self, i):
        pass

    def cons(self, item):
        return NonEmptyList(item, self)

    @classmethod
    def from_list(cls, lst):
        ilist = EmptyList()
        for e in reversed(lst):
            ilist = NonEmptyList(e, ilist)
        return ilist


class EmptyList(ImmutableList):

    def __init__(self):
        pass

    @property
    def head(self):
        return None

    @property
    def tail(self):
        return None

    @property
    def is_empty(self):
        return True

    def reverse(self):
        return self

    def __iter__(self):
        yield None

    def __str__(self):
        return '[]'

    def __len__(self):
        return 0

    def __eq__(self, other):
        return type(other) == EmptyList

    def __hash__(self):
        return 1467932225336596824L

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise ValueError
        raise IndexError('Index out of range.')


class NonEmptyList(ImmutableList):

    def __init__(self, item, lst):
        self._head = item
        self._tail = lst
        self._len = len(lst) + 1

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def is_empty(self):
        return False

    def reverse(self):
        res = EmptyList()
        for e in self:
            res = res.cons(e)
        return res

    def __iter__(self):
        lst = self
        while not lst.is_empty:
            yield lst.head
            lst = lst.tail

    def __str__(self):
        return str(list(self))

    def __len__(self):
        return self._len

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise ValueError
        if  i < -len(self) or len(self) <= i:
            raise IndexError('Index out of range.')
        i %= len(self)
        lst = self
        while i > 0:
            lst = lst.tail
            i -= 1
        return lst.head

    def __eq__(self, other):
        if type(other) != NonEmptyList or len(self) != len(other):
            return False
        g = other.__iter__()
        for e in self:
            if e != g.next(): return False
        return True

    def __hash__(self):
        res = 17
        m = (1 << 64) -1
        for e in self:
            res = (17 * hash(e) + 31) & m
        return res




        
