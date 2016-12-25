class User(object):

    ranks = range(-8, 9)
    ranks.remove(0)
    
    def __init__(self):
        self._rank_idx = 0
        self._progress = 0

    @property
    def rank(self):
        return User.ranks[self._rank_idx]

    @property
    def progress(self):
        return self._progress

    def inc_progress(self, rank):
        idx = User.ranks.index(rank)
        diff = idx - self._rank_idx
        if diff == -1:
            self._progress += 1
        elif diff == 0:
            self._progress += 3
        elif diff > 0:
            self._progress += 10 * diff ** 2
        inc, self._progress = divmod(self._progress, 100)
        self._rank_idx += inc
        if self._rank_idx >= len(User.ranks) - 1:
            self._rank_idx = len(User.ranks) - 1
            self._progress = 0


