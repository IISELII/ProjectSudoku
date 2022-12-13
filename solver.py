
grid =[
        [0, 7, 9, 3, 0, 8, 0, 0, 0],
        [0, 0, 0, 1, 9, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 6, 1, 0, 5, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 9, 0],
        [9, 4, 0, 0, 0, 0, 5, 7, 0],
        [8, 9, 0, 5, 3, 6, 0, 2, 1],
        [0, 0, 0, 0, 0, 7, 0, 6, 4],
        [7, 2, 6, 9, 4, 0, 0, 5, 0]
    ]

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

def solver(grid):
    for x in range(0,9) :
        for y in range(0,9):
            if grid[x][y]==0 :
                for number in range(1,10):
                    if is_possible(grid,number,x,y) :
                        grid[x][y]=number
                        solver(grid)
                        grid[x][y]=0
                return
            else :
                if x==8 and y==8:
                    print(grid)
                    return
