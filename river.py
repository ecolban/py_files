from random import random

def river(w, h):
    return '\n'.join(', '.join('%g' % (2 * random()) for _ in range(w)) for _ in range(h))

class Node(object):

    def __init__(self, r, c, d):
        self.row = r
        self.col = c
        self.depth = d
        self.path_depth = 1.0e6 #infinity
        self.path_length = 1.0e6 #infinity
        self.checked = False
        self.pred = None

    def __lt__(self, other): False

from heapq import heappush, heappop

def shallowest_path(river):

    nodes = [[Node(row, col, float(value)) for col, value in enumerate(line.split(', '))]
             for row, line in enumerate(river.split('\n'))]

    rows = len(nodes)
    cols = len(nodes[0])

    def neighbors(r, c):
        return {nodes[i][j] for i in range(max(0, r - 1), min(rows, r + 2)) 
                            for j in range(max(0, c - 1), min(cols, c + 2)) if i != r or j != c}

    def path_to(node):
        res = []
        while node:
            res.append(node)
            node = node.pred
        res.reverse()
        return res

    visited = []

    # Visit the cells on the left bank
    for node, *_ in nodes:
        node.path_depth, node.path_length = node.depth, 1
        heappush(visited, (node.path_depth, 1, node))

    # If a node is checked, its path_depth is final. 
    # The path_depth of a checked node is less than or equal to the final path_depth of all unchecked nodes.
    while visited:
        pd, pl, node = heappop(visited)
        r, c = node.row, node.col
        if c == cols - 1: return [(n.row, n.col) for n in path_to(node)], pd, pl #right bank reached
        for nb in neighbors(r, c):
            d = max(nb.depth, pd)
            if not nb.checked and (nb.path_depth, nb.path_length) > (d, pl + 1):
                nb.pred = node
                nb.path_depth, nb.path_length = d, pl + 1
                heappush(visited, (d, pl + 1, nb))
        node.checked = True
