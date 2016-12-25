def count_odd_pentaFib(n):
    def pentaFib(a, b, c, d, e, n):
        if n < 5: return [a, b, c, d, e][n]
        else: return pentaFib(b, c, d, e, a + b + c + d + e, n - 1)
    s = {pentaFib(0, 1, 1, 2, 4, i) for i in range(n + 1)}
    return sum(1 for f in s if f % 2 == 1) # (number of odd terms in the "pentafibonacci" sequence)
