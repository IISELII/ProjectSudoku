import numpy as np
import random

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

def col_check(grille):

    col_nb = 0

    for col_nb in range(0, 9):
        col = [index[col_nb] for index in grille]
        for i in range(1, 10):
            if col.count(i) > 1:
                return False

    return True

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

def sudoku_check(grille):
    return row_check(grille) and row_check(find_block(grille)) and col_check(grille)

def difficulty_reading(difficulty) :
    nb_chiffre=0
    if difficulty=='hard' :
        nb_chiffre = 59
    elif difficulty=='medium' :
        nb_chiffre = 46
    else :
        nb_chiffre = 40
    return nb_chiffre

def create_full(grid) :
    grid_created = grid
    for x in range(0,9) :
        randomlist = random.sample(range(1, 10), 9)
        for y in range (0,9) :
            if grid_created[x][y] == 0:
                for number in range (0,9) :
                    if sudoku_check(grid) :
                        grid[x][y]=randomlist[number]
                        if create_full(grid_created) :
                            return True
                        grid_created[x][y] = 0
                return False
    print(grid_created)
    return True

def create_from_full(grid,nb_chiffres_retires,nb_chiffres) :
    x=random.randint(0, 8)
    y=random.randint(0, 8)
    if grid[x][y]==0 :
        create_from_full(grid,nb_chiffres_retires,nb_chiffres)
    else :
        grid[x][y]=0
        nb_chiffres_retires=nb_chiffres_retires+1
        if  nb_chiffres_retires<nb_chiffres :
            create_from_full(grid,nb_chiffres_retires,nb_chiffres)
        else :
            return grid

def creator_sudoku(difficulty) :
    grid=[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    nb_chiffres = difficulty_reading(difficulty)
    create_full(grid)
    create_from_full(grid,0,nb_chiffres)
    return grid

creator_sudoku('easy')
creator_sudoku('medium')
creator_sudoku('hard')
