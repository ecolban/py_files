import re

def solve(input_string):
    pairs = [i.group() for i in re.finditer('[^\n]+', input_string)]
    return '\n'.join(count_carries(*p.split()) for p in pairs)

def count_carries(n1, n2):
    carries = 0
    carry = 0
    s = zip(n1, n2)
    for a, b in reversed(s):
        if int(a) + int(b) + carry > 9:
                carries += 1
                carry = 1
        else:
                carry = 0
    if carries == 0: return 'No carry operation'
    else: return '%d carry operations' % carries

class RomanNumerals:
    symbols = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    rm = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
      (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
      (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
      (1, 'I')]

    @staticmethod
    def to_roman(n):
        s = ""
        for m, r in RomanNumerals.rm:
            while m <= n:
                s += r
                n -=m
        return s

    @staticmethod
    def from_roman(s):
        if not s: return 0
        last = RomanNumerals.symbols[s[0]]
        n = last
        for c in s[1:]:
            if RomanNumerals.symbols[c] > last:
                n -= 2 * last
                last = RomanNumerals.symbols[c]
                n+= last
        return n

def front_back_split(source, front, back):
    if not source or not source.next: raise Exception
    last = front
    runner1 = source
    runner2 = source.next.next
    last.data = runner1.data
    while runner2:
        runner1 = runner1.next
        last.next = Node()
        last = last.next
        last.data = runner1.data
        runner2 = runner2.next
        if runner2: runner2 = runner2.next
    last = back
    runner1 = runner1.next
    last.data = runner1.data
    runner1 = runner1.next
    while runner1:
        last.next = Node()
        last = last.next
        last.data = runner1.data
        runner1 = runner1.next


def zeroes (base, number):
    return min(num_div_factorial(p, number) / exp for p, exp in factors(base))

def num_div_factorial(prime, n):
    '''Returns the number of times that prime divides the factorial of n.'''
    count = 0
    p = prime
    while p <= n:
        count += n / p
        p *= prime
    return count

def factors(n):
    '''Generates the prime factors of n and their associated exponents
       in ascending order of the prime factors.'''
    p = 0
    while n % 2 == 0:
        p +=1
        n /= 2
    if p > 0: yield (2, p)
    f, p = 3, 0
    while f * f <= n:
        if n % f == 0:
            p += 1
            n /= f
        else:
            if p > 0:
                yield(f, p)
                p = 0
            f += 2
    if n == f:
        yield(f, p + 1)
    else:
        if p > 0: yield(f, p)
        if n > 1: yield(n, 1)


    
        

