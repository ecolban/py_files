def unbleach(code):
    return code.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

def remove_comments(code):
    return ''.join(c for c in code if c in ' \t\n')

# solution
def whitespace(code, inp = ''):
    clean_code = unbleach(remove_comments(code))
    ws = WS(clean_code, inp)
    ws.preprocess()
    ws.execute()
    return ws.output

import re

class WS(object):

    NUM = '[st]+n'
    LABEL = '[st]*n'
    
    instructions = {

# Stack manipulation
    'PUSH' : ('ss(%s)' % NUM),
    'DUPLN' : ('sts(%s)' % NUM),
    'DISCN' : ('stn(%s)' % NUM),
    'DUPL' : 'sns',
    'SWAP' : 'snt',
    'DISC' : 'snn',

# Arithmetic
    'ADD' : 'tsss',
    'SUB' : 'tsst',
    'MUL' : 'tssn',
    'DIV' : 'tsts',
    'MOD' : 'tstt',

# Heap access
    'STORE' : 'tts',
    'FETCH' : 'ttt',

# IO
    'WRTC' : 'tnss',
    'WRTI' : 'tnst',
    'RDCH' : 'tnts',
    'RDIN' : 'tntt',

# Flow control
    'MARK' : ('nss(%s)' % LABEL), 
    'CALL' : ('nst(%s)' % LABEL),
    'JMPU' : ('nsn(%s)' % LABEL),
    'JMPZ' : ('nts(%s)' % LABEL),
    'JMPN' : ('ntt(%s)' % LABEL),
    'EXTS' : 'ntn',
    'EXTP' : 'nnn'

    }


    all_instr = {k:re.compile(p) for k,p in instructions.items()}


    def __init__(self, code, inp=''):
        self._code = code
        self._inp = inp
        self._output = ''
        self._stack = []
        self._call_stack = []
        self._heap = {}
        self._labels = self.preprocess()
        self._exit = False   

    def disassemble(self):
        '''Utility function that helps with debugging'''
        num_mnem = ['PUSH', 'DUPLN', 'DISCN']
        label_mnem = ['MARK', 'CALL', 'JMPU', 'JMPZ', 'JMPN']
        code = self._code
        while code:
            mnem, instr = next((k, v) for k, v in WS.all_instr.items() if re.match(v, code))               
            m = re.match(instr, code)
            if mnem in num_mnem:
                num = self._parse_num(m.group(1))
                print ('%s %d' % (mnem, num))
            elif mnem in label_mnem:
                lbl = self._parse_label(m.group(1))
                print ('%s %s' % (mnem, lbl))
            else:
                print(mnem)

            code = code[m.end():]
            
    def preprocess(self):
        '''Builds a dict with the location of all labels that are marked.'''
        code = self._code
        pos = 0
        labels = {}
        while code:
            mnem, instr = next((k, v) for k, v in WS.all_instr.items() if re.match(v, code))               
            m = re.match(instr, code)
            if mnem == 'MARK':
                lbl = self._parse_label(m.group(1))
                assert not lbl in labels
                labels[lbl] = pos + m.end()
            pos += m.end()
            code = code[m.end():]
        return labels

                
    def _parse_num(self, s):
        n = int('0' + ''.join('1' if c == 't' else'0' for c in s[1:-1]), 2)
        return n if s[0] == 's' else -n

    def _parse_label(self, s):
        if len(s) == 1: return '_'
        return s[:-1]
    
           
    def execute(self):
        '''Executes the code from the begining.'''
        pos = 0
        while not self._exit:
            assert pos < len(self._code)
            mnem, instr = next((k, v) for k, v in WS.all_instr.items() if re.match(v, self._code[pos:]))
            m = re.match(instr, self._code[pos:])
            pos += m.end()
            if mnem == 'PUSH':
                n = self._parse_num(m.group(1))
                self._stack.append(n)
            elif mnem == 'DUPLN':
                n = self._parse_num(m.group(1))
                assert 0 <= n and n < len(self._stack) 
                self._stack.append(self._stack[-n - 1])
            elif mnem == 'DISCN':
                n = self._parse_num(m.group(1))
                if n < 0 or n >= len(self._stack):
                    self._stack = self._stack[-1:]
                elif n != 0: 
                    self._stack = self._stack[:-n-1] + [self._stack[-1]]
            elif mnem == 'MARK':
                pass #already preprocessed
            elif mnem == 'CALL':
                self._call_stack.append(pos)
                lbl = self._parse_label(m.group(1))
                pos = self._labels[lbl]
            elif mnem == 'JMPU':
                lbl = self._parse_label(m.group(1))
                pos = self._labels[lbl] 
            elif mnem == 'JMPZ':
                a = self._stack.pop()
                if a == 0:
                    lbl = self._parse_label(m.group(1))
                    pos = self._labels[lbl]
            elif mnem == 'JMPN':
                a = self._stack.pop()
                if a < 0:
                    lbl = self._parse_label(m.group(1))
                    pos = self._labels[lbl]
            elif mnem == 'EXTS':
                pos = self._call_stack.pop()
            elif mnem == 'EXTP':
                self._exit = True
            elif mnem == 'DUPL':
                self._stack.append(self._stack[-1])
            elif mnem == 'DISC':
                self._stack.pop()
            elif mnem == 'SWAP':
                self._stack[-2], self._stack[-1] = self._stack[-1], self._stack[-2]
            elif mnem == 'ADD':
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.append(b + a)
            elif mnem == 'SUB':
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.append(b - a)
            elif mnem == 'MUL':
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.append(b * a)
            elif mnem == 'DIV':
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.append(b / a)
            elif mnem == 'MOD':
                a = self._stack.pop()
                b = self._stack.pop()
                self._stack.append(b % a)
            elif mnem == 'STORE':
                a = self._stack.pop()
                b = self._stack.pop()
                self._heap[b] = a
            elif mnem == 'FETCH':
                a = self._stack.pop()
                b = self._heap[a]
                self._stack.append(b)
            elif mnem == 'WRTC':
                a = self._stack.pop()
                self._output += str(unichr(a))
            elif mnem == 'WRTI':
                a = self._stack.pop()
                self._output += str(a)
            elif mnem == 'RDCH':
                a = self._inp[0]
                self._inp = self._inp[1:]
                b = self._stack.pop()
                self._heap[b] = ord(a)
            elif mnem == 'RDIN':
                a = ''
                idx = 0
                while self._inp[idx] != '\n':
                    a += self._inp[idx]
                    idx += 1
                self._inp = self._inp[idx + 1:]
                b = self._stack.pop()
                self._heap[b] = int(a)
            else:
                raise ValueError('Unknown instruction %s' % mnem)

    @property
    def output(self):
        return self._output




ws = WS('ssstntnttssstsntnttsssttntnttsssttntttssstsntttssstnttttnsttnsttnstnnn', '9\n1\n8\n2\n7\n3\n5\n4\n')

ws.disassemble()

print(ws.preprocess())

ws.execute()

print(ws.output)
        
