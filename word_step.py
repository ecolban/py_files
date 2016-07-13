def word_step(s):
    words = s.split()
    width = sum(len(w) - 1 for w in words[0::2]) + 1
    height = sum(len(w) - 1 for w in words[1::2]) + 1
    res = [[' '] * width for _ in xrange(height)]
    res[0][0] = words[0][0]
    row, col = 0, 0
    row_inc, col_inc = 0, 1
    for w in words:
        for c in w[1:]:
            col += col_inc
            row += row_inc
            res[row][col] = c
        row_inc, col_inc = col_inc, row_inc
    return res

[['S', 'T', 'E', 'P', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', 'S', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', 'T', 'H', 'E', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'I', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', 'T', 'O', 'D', 'A', 'Y']]
