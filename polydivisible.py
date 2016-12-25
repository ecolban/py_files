CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = {c:d for d, c in enumerate(CHARS)}

def is_polydivisible(s, b):
    return all(to_bin(s[:i], b) % i == 0 for i in range(1, len(s) + 1))

def get_polydivisible(n, b):
    count = 0
    while n > 0:
        s = to_str(count, b)
        if is_polydivisible(s, b):
            n -=1
        count += 1
    return s
        

def to_bin(s, b):
    n = 0
    for d in s:
        n *= b
        n += digits[d]
    return n

def to_str(n, b):
    if n == 0: return '0'
    s = ""
    while n > 0:
        n, r = divmod(n, b)
        s = CHARS[r] +  s
    return s

