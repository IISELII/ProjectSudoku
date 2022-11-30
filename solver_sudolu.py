import numpy as np
import math



# def getPossibilities(grid, i,j):
#   # find all the possibilities

#   if not grid[i][j] == 0:
#     return [grid[i][j]]

#   exists = []

#   # find what items can be placed here
#   for k in range(0,9):
#     # what are the items with the same first index
#     lineval = grid[i][k]
#     if lineval not in exists and not lineval == 0:
#       exists.append(lineval)
#     # what are the items with the same second index
#     colval = grid[k][j]
#     if colval not in exists and not colval == 0:
#       exists.append(colval)

#   # what are the items in the same square

#   sq_col = math.floor(i/3) * 3
#   sq_line = math.floor(j/3) * 3

#   for k in range(0,3):
#    for k2 in range(0,3):
#       line = sq_line + k
#       col = sq_col + k2
#       val = grid[col][line]

#       if val not in exists and not val== 0:
#         exists.append(val)
#   available = []


#   for i in range(1,10):
#     if i not in exists:
#       available.append(i)
#   return available

def create_grille(nblignes, nbcolonnes):
    grille = [[]] * nblignes
    for i in range(nblignes):
        grille[i] = [0] * nbcolonnes
    grille = np.array(grille)
    return grille


sudoku_grille = create_grille(9, 9)

sudoku_grille[0][3] = 4
sudoku_grille[0][6] = 8
sudoku_grille[0][7] = 7
sudoku_grille[1][1] = 4
sudoku_grille[1][2] = 7
sudoku_grille[1][4] = 9
sudoku_grille[1][5] = 2
sudoku_grille[1][7] = 5
sudoku_grille[2][0] = 2
sudoku_grille[2][3] = 6
sudoku_grille[2][7] = 3
sudoku_grille[3][0] = 9
sudoku_grille[3][1] = 7
sudoku_grille[3][3] = 5
sudoku_grille[3][6] = 2
sudoku_grille[3][8] = 3
sudoku_grille[4][0] = 5
sudoku_grille[4][2] = 8
sudoku_grille[4][4] = 2
sudoku_grille[4][5] = 4
sudoku_grille[4][6] = 7
sudoku_grille[4][8] = 6
sudoku_grille[5][0] = 6
sudoku_grille[5][2] = 4
sudoku_grille[5][5] = 7
sudoku_grille[5][7] = 8
sudoku_grille[5][8] = 5
sudoku_grille[6][1] = 9
sudoku_grille[6][3] = 3
sudoku_grille[6][5] = 8
sudoku_grille[6][8] = 7
sudoku_grille[7][2] = 3
sudoku_grille[7][3] = 2
sudoku_grille[7][4] = 4
sudoku_grille[7][6] = 1
sudoku_grille[7][7] = 6
sudoku_grille[8][1] = 1
sudoku_grille[8][2] = 2
sudoku_grille[8][7] = 9

print(sudoku_grille)
