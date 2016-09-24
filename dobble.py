p = 7

gf = range(p)

points = {(x, y) for x in gf for y in gf}

directions = {(1, y) for y in gf} | {(0, 1)}

lines = {(a, b, c) for (a, b) in directions for c in gf}

line_nums = {line:n for n, line in enumerate(lines)}

cards_fin = {tuple(line_nums[(a, b, (a * x + b * y) % p)] for (a, b) in directions) for (x, y) in points}

line_at_infinity = len(line_nums)

cards_inf = {tuple(line_nums[(a, b, c)] for c in gf) + (line_at_infinity,) for (a, b) in directions}

cards = cards_fin | cards_inf

#====================================================
# OUTPUT
#====================================================

# pix = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + list('@#$%&')
# for c in cards: print(' '.join(pix[i] for i in c))

frmt = '%%0%dd' % len(str(line_at_infinity))
for c in cards: print(' '.join(frmt % i for i in c))
