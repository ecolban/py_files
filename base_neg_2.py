def from_decimal(n):
    if n == 0: return '0'
    res = '' 
    while n != 0:
        n, b = divmod(n, -2)
        if b == -1: n, b = n + 1, 1
        res = str(b) + res
    return res

def from_binary(s):
    res = 0
    for b in s:
        res = res * -2 + int(b)
    return res
    
