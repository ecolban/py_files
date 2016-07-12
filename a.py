def fibonacci_recursive(n):
    def fib(a, b, k):
        if k > 1: return fib(b, a + b, k - 1)
        if k == 1: return b
        return a
    return fib(0, 1, n)

def fibonacci_loop(n):
    a, b = 0, 1
    while n > 0:
        a, b, n = b, a + b, n - 1
    return a

        
