import numpy as np
import random
# Create a grille


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






# def random_number(myarray, how_much_number):
#     for i in range(myarray):
#         myarray = myarray[i] * np.random.random_sample(how_much_number)
#     return myarray




# print(random_number(sudoku_grille, 10))


# create the conditions

# class SudokuGrille:


#     def __init__(self, nblignes, nbcolonnes):
#         self.nblignes = nblignes
#         self.nbcolonnes = nbcolonnes


#     def create_a_grille(self, nblignes, nbcolonnes):
#         grille = [[]] * nblignes
#         for i in range(nblignes):
#             grille[i] = [0] * nbcolonnes
#         grille = np.array(grille)
#         return grille


# grille = SudokuGrille(9, 9)
# print(grille)
