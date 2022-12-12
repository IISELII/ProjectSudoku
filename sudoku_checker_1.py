import random
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
        if len(grille[row_nb]) == 9:
            for i in range(1, 10):
                if grille[row_nb].count(i) == 1:
                    True
                elif grille[row_nb].count(i) > 1:
                    print(f"{i} have doublon at row {row_nb}")
                    return False

        else:
            print(f"The length of the row {row_nb} is not OK")
            return False

    return True


def col_check(grille):

    col_nb = 0

    for col_nb in range(0, 9):
        col = [index[col_nb] for index in grille]
        if len(col) == 9:
            for i in range(1, 10):
                if col.count(i) == 1:
                    True
                elif col.count(i) > 1:
                    print(f"{i} have doublon at column {col_nb}")
                    return False

        else:
            print(f"the length of the column {col_nb+1} is not OK")
            return False

    return True


def bloc(x,y) :
    X=x//3
    Y=y//3
    return X,Y

def find_block(grid,x,y) :
    X,Y=bloc(x,y)
    l1=[]
    for X in range(0,3) :
        for Y in range (0,3) :
            l2=[]
            for x in range (0,3) :
                for y in range (0,3) :
                    l2.append(grid[X * 3+x][Y * 3+y])
            l1.append(l2)
    return l1

def group(grid):
    res = True
    new_grid =find_block(grid,0,0)
    for i in range(0,9):
        blocs = new_grid[i]
        for j in range(1,10):
            if blocs.count(j) > 1:
                return False
            if blocs.count(j) == 1:
                res = True
    return res


def sudoku_checker(grille):

    if row_check(grille):
        print(row_check(grille))

    if col_check(grille):
        print(col_check(grille))

    if group(grille):
        print(group(grille))

    final = print("Le Sudoku a fini d'être vérifié !!")
    return final


print(sudoku_checker(sudoku_1))
