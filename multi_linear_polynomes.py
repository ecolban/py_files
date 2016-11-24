import re
def simplify(poly):
    pattern = r'([+-]?)(\d*)([a-z]+)'
    it = re.finditer(pattern, poly)
    monomes = {}
    for m in it:
        sign = -1 if m.group(1) == '-' else 1
        coeff = int(m.group(2)) if m.group(2) else 1
        vs = ''.join(sorted(list(m.group(3))))
        monomes[vs] = monomes.get(vs, 0) + sign * coeff
    items = sorted(((vs, coeff) for (vs, coeff) in monomes.items() if coeff != 0), key=lambda x: (len(x[0]), x[0]))
    output = ''.join('%s%s%s' % ('+' if coeff > 0 else '-', abs(coeff) if abs(coeff) != 1 else '', vs)
                     for (vs, coeff) in items)
    return output[1:] if output[0] == '+' else output
