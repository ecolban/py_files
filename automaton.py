class Automaton(object):

    def __init__(self):
        self.states = {
                ('q1', '0'): 'q1', ('q1', '1'): 'q2',
                ('q2', '0'): 'q3', ('q2', '1'): 'q2',
                ('q3', '0'): 'q2', ('q3', '1'): 'q2'}

    def read_commands(self, commands):
        state = 'q1'
        for c in commands:
            state = self.states[(state, c)]
        return state == 'q2'

my_automaton = Automaton()


s = '1234'

def goodVsEvil(good, evil):
    good_vals = [1, 2, 3, 3, 4, 10]
    evil_vals = [1, 2, 2, 2, 3, 5, 10]
    good = map(int, good.split())
    evil = map(int, evil.split())
    good_total = sum(map(lambda (x, y): x * y, zip(good, good_vals)))
    evil_total = sum(map(lambda (x, y): x * y, zip(evil, evil_vals)))
    if good_total > evil_total:
        return 'Battle Result: Good triumphs over Evil'
    if good_total < evil_total:
        return 'Battle result: Evil eradicates all trace of Good'
    return 'Battle Result: No victor on this battle field'


def permutations(string):
    if len(string) < 2: return [string]
    d = {string[i] : string[:i] + string[i+1:] for i in range(len(string))}
    return [k + x for k in d.keys() for x in permutations(d[k])]

def gap(g, m, n):
    p1 = next_prime(m, n)
    if not p1: return None
    print(p1)
    found = False
    while not found:
        p2 = next_prime(p1 + 2, n)
        if not p2: return None
        if p1 + g == p2: found = True
        else: p1 = p2
    return [p1,p2]

def next_prime(m, n):
    k = m if m == 2 or m % 2 == 1 else m + 1
    while k <= n:
        if is_prime(k): return k
        k += 2
    return None

def is_prime(k):
    low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 
                53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 
                113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 
                181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
                251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 
                317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 
                397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 
                463, 467, 479, 487, 491, 499]
    if k in low_primes: return True
    for p in low_primes:
        if k % p == 0: return False
    return rabin_miller(k)

import random

def rabin_miller(num):
     s = num - 1
     t = 0
     while s % 2 == 0:
         s /= 2
         t += 1

     for trials in range(5): # try to falsify num's primality 5 times
         a = random.randrange(2, num - 1)
         v = pow(a, s, num)
         if v != 1: # this test does not apply if v is 1.
             i = 0
             while v != (num - 1):
                 if i == t - 1:
                     return False
                 else:
                     i = i + 1
                     v = (v ** 2) % num
     return True



from random import randint

def prime(n):
    for _ in xrange(7):
        if pow(randint(1,n-1),n-1,n) != 1:return False
    return True

##def next_prime(n):
##    n += 1 if n % 2 == 0 else 2
##    while not prime(n):n+=2
##    return n


##def gap(g, m, n):
##    a = m if prime(m) else next_prime(m)
##    b = next_prime(a)
##    while b <= n:
##        if b - a == g:return [a,b]
##        a,b = b,next_prime(b)
