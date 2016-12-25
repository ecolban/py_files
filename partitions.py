def partitions(n):

    d = {}

    def part_h(k, m):
        if k == 0: return 1
        if m <= 0: return 0
        if not (k, m) in d:
            d[(k, m)] = part_h(k - m, min(k - m, m)) + part_h(k, m - 1)
        return d[(k, m)]

    return part_h(n, n)

    
