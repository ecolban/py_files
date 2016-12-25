def is_possible(puzzle, row, col, v):
    '''Checks if it possible to add a value v in row row and column col.'''
    for k in xrange(9):
        if puzzle[row][k] == v or puzzle[k][col] == v:
            return False
    row0 = row - row % 3
    col0 = col - col % 3
    for i in xrange(row0, row0 + 3):
        for j in xrange(col0, col0 + 3):
            if puzzle[i][j] == v: return False
    return True
    
def find_empty_space(puzzle):
    '''Returns a space with a minimum of possible value assignments'''
    min_possibilities = 10
    min_space= None
    for row in xrange(9):
        for col in xrange(9):
            if puzzle[row][col] == 0:
                possibilities = 0
                for v in xrange(1, 10):
                    if is_possible(puzzle, row, col, v): possibilities += 1
                if possibilities < min_possibilities:
                    min_possibilities = possibilities
                    min_space = (row, col)
    return min_space
        

def sudoku(puzzle):
    """If puzzle is solvable, return the solved puzzle as a 2d array 
       of 9 x 9. Otherwise, return None. When returning None, the puzzle is 
       in the same state as when this function was called. """
    space = find_empty_space(puzzle)
    if space == None: return puzzle #no empty spaces means puzzle is solved!
    row, col = space
    for v in xrange(1,10):
        if is_possible(puzzle, row, col, v):
            puzzle[row][col] = v
            solution = sudoku(puzzle)
            if solution != None: return solution
    puzzle[row][col] = 0 # make sure that the puzzle is back in its initial state
    return None

puzzle1 = [[0, 0, 9, 0, 0, 7, 0, 1, 0],
           [0, 4, 0, 3, 0, 9, 2, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 3],
           [0, 6, 0, 8, 0, 0, 0, 9, 0],
           [3, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 2, 0, 0, 0, 5, 0, 7, 0],
           [4, 0, 0, 0, 8, 0, 0, 0, 0],
           [0, 0, 2, 5, 0, 4, 0, 8, 0],
           [0, 8, 0, 7, 0, 0, 4, 0, 0]]

solution = [[5, 3, 9, 6, 2, 7, 8, 1, 4],
            [8, 4, 1, 3, 5, 9, 2, 6, 7],
            [2, 7, 6, 4, 1, 8, 9, 5, 3],
            [1, 6, 7, 8, 4, 3, 5, 9, 2],
            [3, 5, 8, 9, 7, 2, 6, 4, 1],
            [9, 2, 4, 1, 6, 5, 3, 7, 8],
            [4, 1, 5, 2, 8, 6, 7, 3, 9],
            [7, 9, 2, 5, 3, 4, 1, 8, 6],
            [6, 8, 3, 7, 9, 1, 4, 2, 5]]

m = all(puzzle1[i][j] == 0 or puzzle1[i][j] == solution[i][j]
    for i in range(9) for j in range(9))
