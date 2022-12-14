def is_possible_row(grid,number,x):
    for i in range (0,9) :
        if grid[x][i]==number : return False
    return True

def is_possible_column(grid,number,y):
    for i in range (0,9) :
        if grid[i][y]==number : return False
    return True

def block(x,y) :
    X=x//3
    Y=y//3
    return X,Y

def is_possible_block(grid,number,x,y) :
    X,Y=block(x,y)
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[X*3+i][Y*3+j]==number : 
                return False
    return True

def is_possible(grid,number,x,y) :
    return is_possible_row(grid,number,x) and is_possible_column(grid,number,y) and is_possible_block(grid,number,x,y)


#Ce solver est plus opti car il s'arrête dès qu'il a trouvé une solution. Il change aussi la grille de sudoku
#Ce qui permet de la stocker.

def solver(grid):
    grid_solved = grid
    for x in range(0,9):
        for y in range(0,9):
            if grid_solved[x][y] == 0:
                for number in range(1,10):
                    if is_possible(grid_solved, number, x, y):
                        grid_solved[x][y] = number
                        if solver(grid_solved):
                            return True
                        grid_solved[x][y] = 0
                return False
    print(grid_solved)
    return True