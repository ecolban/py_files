def gray1(n):
    
    def gray_h (n, p):
        assert n < p
        if p == 2: return str(n)
        if n >= p / 2: return '1' + gray_h(p - n - 1, p / 2)
        return '0' + gray_h(n, p / 2)

    p = max(2, 1 << (n).bit_length())
    return gray_h(n, p)


def gray2(n):
    p, s = 2 ** (n).bit_length(), 0
    while p > 2:
        s <<= 1
        if n >= p / 2:
            s += 1
            n = p - n - 1
        p >>= 1
    return (s << 1) + n

def gray3(n):
    if n < 2: return str(n)
    return gray3(n >> 1) + str((n ^ (n >> 1)) & 1)


def gray4(n):
    s = ''
    p = 1
    while n > 1:
        s = ('1' if n & 3 in (1, 2) else '0') + s
        n >>= 1
    return str(n) + s

def gray5(n):
    return n ^ (n >> 1)

def gray_inv(n):
    b = 0 #next bit to append to result
    p = 1 << (n).bit_length() #power of 2 greater than n
    result = 0
    while p > 1:
        p >>= 1
        if n & p != 0: b = 1 - b #flip bit when a 1 is in corresponding bit position in n
        result = (result << 1) | b
    return result

    
