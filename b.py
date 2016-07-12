def fibonacci(n):
    a, b = 0, 1
    while n > 0:
        a, b, n = b, a + b, n - 1
    return a
