def padovan(n):
    a, b, c = 1, 0, 0
    for x in bin(n + 3)[2:]:
        a, b, c = a * a + 2 * b * c, (2 * a  + b) * b + c * c, b * b + 2 * (a + b) * c
        if x == '1': a, b, c = b, c, a + b
    return c
