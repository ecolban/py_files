p = 7

gf = range(p)

points = {(x, y) for x in gf for y in gf}

directions = {(1, b) for b in gf} | {(0, 1)}

lines = {(a, b, c) for (a, b) in directions for c in gf}

line_nums = {line:n for n, line in enumerate(lines)}

cards_fin = {tuple(line_nums[(a, b, (a * x + b * y) % p)] for (a, b) in directions) for (x, y) in points}

line_at_infinity = len(line_nums)

cards_inf = {tuple(line_nums[(a, b, c)] for c in gf) + (line_at_infinity,) for (a, b) in directions}

cards = cards_fin | cards_inf

#====================================================
# OUTPUT
#====================================================

card_format = '%%0%dd' % len(str(line_at_infinity))
for c in cards: 
    print(' '.join(card_format % i for i in c))
