def brain_luck(code, inp):
    code_p, data_p = 0, 0
    inp, output, data = iter(inp), '', [0]
    brackets = preprocess(code)
    while code_p < len(code):
        c = code[code_p]
        if c == '>':
            data_p += 1
            if data_p >= len(data): data += [0]
        elif c == '<':
            if data_p == 0: data = [0] + data
            else: data_p -= 1
        elif c == '+': data[data_p] = (data[data_p] + 1) % 256
        elif c == '-': data[data_p] = (data[data_p] - 1) % 256
        elif c == ',': data[data_p] = ord(next(inp))
        elif c == '.': output += chr(data[data_p])
        elif c == '[' and data[data_p] == 0: code_p = brackets[code_p]
        elif c == ']' and data[data_p] != 0: code_p = brackets[code_p]
        code_p += 1
    return output

def preprocess(code):
    stack, res = [], {}
    for idx, c in enumerate(code):
        if c == '[': stack.append(idx)
        elif c == ']':
            m_idx = stack.pop()
            res[m_idx], res[idx] = idx, m_idx
    assert not stack
    return res



code = ',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]'
inp = '\n'


output = brain_luck(code, inp)
print(output)


def divisors(n):
    divs = set([1])
    fact = 2
    while fact * fact <= n:
        if n % fact == 0:
            divs.add(fact)
            divs.add(n / fact)
        fact += 1
    return divs



def perm(w):
    if len(w) == 1: return [w]
    else:
        d = {c:p for p, c in enumerate(w)}
        return [c + v for c in d.keys() for v in perm(w[:d[c]] + w[d[c] + 1:])]


def perm2(w):
    if len(w) == 1: return [w]
    else:
        return [w[p] + v for p in range(len(w)) for v in perm2(w[:p] + w[p + 1:])]



class Morse:
    
    MAX_INT = 0x7fffffff
    MODULUS = 1 << 32
    
    @classmethod
    def encode(self, message):
        words = message.split()
        s = '0000000'.join('000'.join(Morse.alpha[c] for c in w) for w in words)
        r = len(s) % 32
        if r > 0: s += ('0' * (32 - r))
        slices = [int(s[i:i+32], 2) for i in range(0, len(s), 32)]
        return [n if n <= Morse.MAX_INT else n - Morse.MODULUS for n in slices]

    @classmethod
    def decode(self, array):
        s_parts = [bin(n + Morse.MODULUS if n < 0 else n)[2:] for n in array]
        s = ''.join('0' * (32 - len(c)) + c for c in s_parts).rstrip('0')
        return ' '.join(''.join(Morse.alpha_inv[c] for c in w.split('000')) \
                       for w in s.split('0000000'))

    alpha={
  'A': '10111',
  'B': '111010101',
  'C': '11101011101',
  'D': '1110101',
  'E': '1',
  'F': '101011101',
  'G': '111011101',
  'H': '1010101',
  'I': '101',
  'J': '1011101110111',
  'K': '111010111',
  'L': '101110101',
  'M': '1110111',
  'N': '11101',
  'O': '11101110111',
  'P': '10111011101',
  'Q': '1110111010111',
  'R': '1011101',
  'S': '10101',
  'T': '111',
  'U': '1010111',
  'V': '101010111',
  'W': '101110111',
  'X': '11101010111',
  'Y': '1110101110111',
  'Z': '11101110101',
  '0': '1110111011101110111',
  '1': '10111011101110111',
  '2': '101011101110111',
  '3': '1010101110111',
  '4': '10101010111',
  '5': '101010101',
  '6': '11101010101',
  '7': '1110111010101',
  '8': '111011101110101',
  '9': '11101110111011101',
  '.': '10111010111010111',
  ',': '1110111010101110111',
  '?': '101011101110101',
  "'": '1011101110111011101',
  '!': '1110101110101110111',
  '/': '1110101011101',
  '(': '111010111011101',
  ')': '1110101110111010111',
  '&': '10111010101',
  ':': '11101110111010101',
  ';': '11101011101011101',
  '=': '1110101010111',
  '+': '1011101011101',
  '-': '111010101010111',
  '_': '10101110111010111',
  '"': '101110101011101',
  '$': '10101011101010111',
  '@': '10111011101011101',
  ' ': '0'}
    alpha_inv = {v:k for k, v in alpha.items()}
