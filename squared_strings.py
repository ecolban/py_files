import math

def pad(s):
    n = int(math.ceil(math.sqrt(len(s))))
    s += chr(11) * (n * n - len(s))
#    s = '\n'.join(s[i:i + n] for i in range(0, n * n, n))
    return s, n

def rotate_cw(s, n):
    # (r, c) <= (n - 1 - c, r)
    return '\n'.join(''.join(s[(n - 1 - c) * n + r] for c in range(n)) 
                        for r in range(n)) 

def rotate_ccw(s, n):
    # (r, c) <= (c, n - 1 - r)
    return '\n'.join(''.join(s[c * n + n - 1 - r] for c in range(n))
                        for r in range(n))

def flatten(s):
    return ''.join(s.split('\n'))

def encode (s):
    s, n = pad(s)
    return rotate_cw(s, n)

def decode(s):
    # your code
    pass

s = "I was going fishing that morning at ten o'clock" 

# "c nhsoI\nltiahi \noentinw\ncng nga\nk mg s\n\voao f \n\v'trtig"

 

