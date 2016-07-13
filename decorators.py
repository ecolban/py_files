def memoize(f):
    memo = {}
    def memoized(*args):
        if not args in memo:
            memo[args] = f(*args)
        return memo[args]
    return memoized

    
    


