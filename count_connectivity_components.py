from collections import Counter
from union_find import Component

def components(grid):
    rs = grid.split('\n')
    cols = rs[0].count('+') - 1
    rows = len(rs) // 2
    comps = {(r, c):Component() for r in range(rows) for c in range(cols)}

    def noWallOnRight(r, c):
        return rs[2 * r + 1][3 * c + 3] == ' '

    def noWallBelow(r, c):
        return rs[2 * (r + 1)][3 * c + 1: 3 * c + 3] == '  '

    for r in range(rows):
        for c in range(cols):
            if noWallOnRight(r, c): comps[(r, c)].union(comps[(r, c + 1)])
            if noWallBelow(r, c):   comps[(r, c)].union(comps[(r + 1, c)])

    for r in range(rows):
        for c in range(cols):
            comps[(r, c)] = comps[(r, c)].find()

    return sorted(Counter(Counter(comps.values()).values()).items(), reverse=True)

from random import randrange

class Edge(object):
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.cost = randrange(10) + 1

class Node(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

def generate_grid(rows, cols, n):
##    assert n <= 2 * rows * cols - rows - cols
    assert n < rows * cols
    nodes = [[Node(r, c) for c in range(cols)] for r in range(rows)]
    v_edges = {Edge(nodes[r][c], nodes[r][c + 1]) for c in range(cols - 1) for r in range(rows)}
    h_edges = {Edge(nodes[r][c], nodes[r + 1][c]) for c in range(cols) for r in range(rows - 1)}
    all_edges = v_edges | h_edges
    sorted_edges = sorted(all_edges, key=lambda e: e.cost)
    comps = {node:Component() for row in nodes for node in row}
    def select_edges():
        s_edges = set()
        edge_gen = (e for e in sorted_edges)
        selected = 0
        while selected < n:
            e = next(edge_gen)
            if comps[e.u].find() != comps[e.v].find():
                comps[e.u].union(comps[e.v])
                s_edges.add((e.u.row, e.u.col, 'v' if e.u.row == e.v.row else 'h'))
                selected += 1
        return s_edges

    def grid(edges):
        lines = []
        lines.append('+' + '--+' * cols)
        for r in range(rows):
            lines.append('|' + ''.join('   ' if (r, c, 'v') in edges else '  |' for c in range(cols)))
            lines.append('+' + ''.join('  +' if (r, c, 'h') in edges else '--+' for c in range(cols)))
        return '\n'.join(lines)
        
    return grid(select_edges())


