class Number(object):

    def __init__(self, i):
        self.a = i


class Number_(Number):

    def __add__(self, other):
        return Number_(self.a + other.a)

    def __str__(self):
        return str(self.a)



