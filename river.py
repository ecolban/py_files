from random import randrange

def river(w, h):
    return '\n'.join(', '.join('%0.1f' % (randrange(21) / 10.0) for _ in range(w)) for _ in range(h))

class Node(object):

    def __init__(self, r, c, d):
        self.row = r
        self.col = c
        self.depth = d
        self.path_depth = 1.0e6 #infinity
        self.checked = False
        self.pred = None

    def __lt__(self, other):
        return self.path_depth < other.path_depth

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
        result = []
        while node:
            result.append(node)
            node = node.pred
        return [(n.row, n.col, n.depth) for n in reversed(result)]

    visited = []

    # Visit the cells on the left bank
    for r in range(len(nodes)):
        nodes[r][0].path_depth = nodes[r][0].depth
        heappush(visited, nodes[r][0])

    # If a node is checked, its path_depth is final. 
    # The path_depth of a checked node is less than or equal to the final path_depth of all unchecked nodes.
    while visited:
        node = heappop(visited)
        node.checked = True
        r, c, pd = node.row, node.col, node.path_depth
        if c == cols - 1: return path_to(node), pd #right bank reached
        for nb in neighbors(r, c):
            if not nb.checked and pd < nb.path_depth and nb.depth < nb.path_depth:
                nb.path_depth = max(nb.depth, pd)
                nb.pred = node
                heappush(visited, nb)
