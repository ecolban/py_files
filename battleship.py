def validateBattlefield(field):
    ships = []
    for r in xrange(10):
        for c in xrange(10):
            if field[r][c] == 1:
               for i in [-1, 1]:
                   if 0 <= r + i and r + i < 10:
                       for j in [-1, 1]:
                          if 0 <= c + j and c + j < 10 and field[r+i][c+j] == 1:
                              return False
                            
                        
                        
            if any(s for s in ships if adj(s, r, c)):
                s = next(s in ships if adj(s, r, c))
                s.append((r, c))
            else:
                ships.append([(r,c)])
    return map(len, ships).sort() == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
               

#def adj(s, r, c):
               
                
