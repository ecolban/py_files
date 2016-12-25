def toAscii85(data):
    # Encode data to ASCII85
    blocks = [data[i:i+4] for i in range(0, len(data), 4)]    
    return '<~' + ''.join(encodeBlock(b) for b in blocks) + '~>'
    
def fromAscii85(data):
    # Decode data from ASCII85
    data = data.replace('z', '!!!!!')
    data = ''.join(data.split())
    data = data[2:-2]
    blocks = [data[i:i+5] for i in range(0, len(data), 5)]
    return ''.join(decodeBlock(b) for b in blocks)


def encodeBlock(b):
    if b == '\x00' * 4: return 'z'
    n = 0
    p = 0
    for i in range(4):
        n <<= 8
        if i < len(b): n += ord(b[i])
        else: p += 1
    res = ''
    for i in range(5):
        c = chr(n % 85 + 33)
        res = c + res
        n /= 85
    return res  if p == 0 else res[:-p]


def decodeBlock(s):
    n = 0
    p = 0
    for i in range(5):
        n *= 85
        if i < len(s): n += ord(s[i]) - 33
        else:
 #           n += ord('u') - 33
            p += 1
    res = ''
    for i in range(4):
        res = chr(n & 0xff) + res
        n >>= 8
    return res if p == 0 else res[:-p]
