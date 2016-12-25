def get_neighbors_alive(cells, r, c):
    return sum(cells[i][j] for i in range(r - 1, r + 2) if 0 <= i and i < len(cells)
        for j in range(c - 1, c + 2) if 0 <= j and j < len(cells[0])) - cells[r][c]
    
def extend_space(cells):
    num_cols = len(cells[0])
    new_cells = [[0] * (num_cols + 2)] +\
                [[0] + row + [0] for row in cells] +\
                [[0] * (num_cols + 2)]
    return new_cells

def shave_space(cells):
    while all(c == 0 for c in cells[0]): cells = cells[1:]
    while all(c == 0 for c in cells[-1]): cells = cells[:-1]
    while all(r[0] == 0 for r in cells): cells = [r[1:] for r in cells]
    while all(r[-1] == 0 for r in cells): cells = [r[:-1] for r in cells]
    return [[]] if cells == [] else cells

def get_generation(cells, generations):
    for count in range(generations):
        cells = extend_space(cells)
        next_cells = [[0 for c in cells[0]] for r in cells]
        for r in xrange(len(cells)):
            for c in xrange(len(cells[0])):
                alive = get_neighbors_alive(cells, r, c)
                if cells[r][c] == 1 and alive == 2 or alive == 3\
                   or cells[r][c] == 0 and alive == 3:
                    next_cells[r][c] = 1
                else:
                    next_cells[r][c] = 0
        cells = shave_space(next_cells)
    return cells
                    

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]

