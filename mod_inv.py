def mod_inv(n, m):
    x, y, k = 0, 1, m
    while n > 0:
        q, r = divmod(k, n)
        x, y, k, n = y, x - q * y, n, r
    if k > 1: return None
    return m + x if x < 0 else x
    
