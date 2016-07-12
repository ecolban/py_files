def fibonacci(n):
    def fib(a, b, k):
        if k > 1: return fib(b, a + b, k - 1)
        if k == 1: return b
        return a
    return fib(0, 1, n)

        
