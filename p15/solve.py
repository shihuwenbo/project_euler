def count_path(r, c):
    grid = list()
    for i in xrange(0,r+1):
        grid.append([0]*(c+1))
    
    for i in xrange(0,c+1):
        grid[0][i] = 1
    for i in xrange(0,r+1):
        grid[i][0] = 1
    
    for i in xrange(1,r+1):
        for j in xrange(1,c+1):
            grid[i][j] = grid[i-1][j]+grid[i][j-1]

    return grid[r][c]

print count_path(20, 20)
