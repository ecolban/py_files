def isPrime(n):
     return n == 2 or n > 2 and n % 2 != 0 and all(n % k != 0 for k in range(3, int(n ** 0.5) + 1, 2))

def step(g, m, n):
    return next(([x, x + g] for x in range(m, n - g + 1) if isPrime(x) and isPrime(x + g)), None)
