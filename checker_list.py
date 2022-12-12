import numpy as np
# créer les grilles de sudoku
grid1 =  [
        [7, 0, 0, 0, 0, 0, 0, 9, 0],
        [2, 4, 5, 1, 9, 0, 0, 8, 0],
        [3, 8, 6, 0, 0, 0, 6, 0, 0],
        [4, 6, 1, 0, 5, 0, 8, 0, 0],
        [5, 0, 0, 0, 0, 3, 0, 9, 0],
        [9, 4, 0, 0, 0, 0, 5, 7, 0],
        [8, 9, 0, 5, 3, 6, 0, 2, 1],
        [6, 0, 0, 0, 0, 7, 0, 6, 4],
        [1, 7, 9, 3, 2, 8, 4, 5, 6]
    ]

sudoku_1 = [[4, 7, 9, 3, 6, 8, 2, 1, 5],
            [6, 3, 2, 1, 9, 5, 4, 8, 7],
            [1, 8, 5, 2, 7, 4, 6, 3, 9],
            [3, 6, 1, 7, 5, 9, 8, 4, 2],
            [2, 5, 7, 4, 8, 3, 1, 9, 6],
            [9, 4, 8, 6, 1, 2, 5, 7, 3],
            [8, 9, 4, 5, 3, 6, 7, 2, 1],
            [5, 1, 3, 8, 2, 7, 9, 6, 4],
            [7, 2, 6, 9, 4, 1, 3, 5, 8]]

# definir la fonction qui vérifie la ligne

def row_check(grille):

    row_nb = 0

    for row_nb in range(0, 9):
            for i in range(1, 10):
                if grille[row_nb].count(i) > 1:
                    return False
    return True


def col_check(grille):

    col_nb = 0

    for col_nb in range(0, 9):
        col = [index[col_nb] for index in grille]
        for i in range(1, 10):
            if col.count(i) > 1:
                return False

    return True


def bloc(x,y) :
    X=x//3
    Y=y//3
    return X,Y

def find_block(grille) :
    l1=[]
    for X in range(0,3) :
        for Y in range (0,3) :
            l2=[]
            for x in range (0,3) :
                for y in range (0,3) :
                    l2.append(grille[X * 3+x][Y * 3+y])
            l1.append(l2)
    return l1

def find_blockvt(grid) :
    for X in range(0,3) :
        for Y in range (0,3) :
            liste=[]
            for x in range (0,3) :
                for y in range (0,3) :
                    liste.append(grid[X * 3+x][Y * 3+y])
            print(liste)

    return True

def sudoku_check(grille):
    return row_check(grille) and row_check(find_block(grille)) and col_check(grille)


import time
start_time = time.time()
sudoku_check(sudoku_1)
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)
