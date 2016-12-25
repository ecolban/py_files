from random import randrange
def is_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    if n < 2: return False
    if n in primes: return True
    if any(n % p == 0 for p in primes): return False
    if n <= 10201: return True
    
    def rabin_miller(n):
        d, s = n - 1, 0
        while d & 1 == 0:
            d >>= 1
            s += 1

        def witness(w):
            return not (pow(w, d, n) == 1 or any(pow(w, d << r, n) == n - 1 for r in range(s)))

##        def witness(w):
##            a = pow(w, d, n)
##            if a == 1 or a == n - 1:
##                return False
##            for r in range(1, s):
##                a = a * a % n
##                if a == n - 1:
##                    return False
##            return True
    
        return not any(witness(randrange(2, n - 1)) for _ in range(10))

    return rabin_miller(n)


def witness(w, n):
    d, s, = n - 1, 0
    while d & 1 == 0:
        d >>= 1
        s += 1
    a = pow(w, d, n)
    if a == 1 or a == n - 1: return False
    for r in range(1, s):
        a = a * a % n
        assert a == pow(w, d << r, n)
        if a == n - 1: return False
    return True


n = 10560454437032556550330308922701395998231880613737780674520416596382340747893415930200889933469377586733381444911191518299699078241334658449342731435981748146854516764736151913072537445350780189809933417773832254097775211653945973228765272285149773266006880385815511626651861121823858077041317173976741
m = next(i for i in range(n + 2, n + 1000, 2) if is_prime(i))
print(m)
