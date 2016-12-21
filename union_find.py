class Component(object):

    def __init__(self):
        self.parent = None
        self.rank = 0

    def union(self, c2):
        c1 = self.find()
        c2 = c2.find()
        if c1 == c2: return
        if c1.rank < c2.rank:
            c1.parent = c2
        elif c2.rank < c1.rank:
            c2.parent = c1
        else:
            c2.parent = c1
            c1.rank += 1

    def find(self):
        if self.parent == None:
            return self
        else:
            self.parent = self.parent.find()
            return self.parent

