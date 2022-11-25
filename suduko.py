# SAMPLE GRID
grid = [
    [0,0,0,  7,0,0,  0,0,0],
    [1,0,0,  0,0,0,  0,0,0],
    [0,0,0,  4,3,0,  2,0,0],

    [0,0,0,  0,0,0,  0,0,6],
    [0,0,0,  5,0,9,  0,0,0],
    [0,0,0,  0,0,0,  4,1,8],

    [0,0,0,  0,8,1,  0,0,0],
    [0,0,2,  0,0,0,  0,5,0],
    [0,4,0,  0,0,0,  3,0,0]
]

Status = False

def printGrid(grid):
    """ PRINTING GRID """
    for i in range(0, 9):
        if i in [3, 6]:
            print('')
        for j in range(0, 9):
            if j in [3, 6]:
                print('  ', end='')
            print(grid[i][j], end=' ')

        print()



""" FUNCTION TO CHECK EACH NUMBER WHETHER IT IS LEGAL OR NOT """

def isValidEntry(grid, value, y, x):
    for i in range(0,9):
        if grid[i][x] == value or grid[y][i] == value:
            return False

    X = 3*(x//3)
    Y = 3*(y//3)

    for i in range(Y,Y+3):
        for j in range(X,X+3):
            if grid[i][j] == value:
                return False

    return True

""" FUNCTION FOR RECURSIVE CALL """

def solveSudoko(grid, i, j):

    if i == 8 and j == 8:
        return  True

    if j < 8:
        j += 1
    elif j == 8 and i < 8:
        j = 0
        i += 1


    if grid[i][j] == 0:
        for value in range(1,10):
            if isValidEntry(grid, value, i, j):
                grid[i][j] = value
                status = solveSudoko(grid,i,j)

                if status:
                    return status
        grid[i][j] = 0
        return

    else:
        status = solveSudoko(grid,i,j)
        return status

def solve(grid):
    i=j=0
    if grid[i][j] == 0:
        for value in range(1,10):
            if isValidEntry(grid, value, i, j):
                grid[i][j] = value
                status = solveSudoko(grid, i, j)
    else:
        Status = solveSudoko(grid, i, j)


if __name__ == '__main__':
    print('Solving...')
    print('Please have patience, It may take some TIME Based on Difficulty level of the problem')
    print('')
    solve(grid)
    if Status:
        printGrid(grid)
    else:
        print('No Solution Exist With this GRID')