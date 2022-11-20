import numpy as np
import random
# Create a grille


def create_grille(nblignes, nbcolonnes):
    grille = [[]] * nblignes
    for i in range(nblignes):
        grille[i] = [0] * nbcolonnes
    grille = np.array(grille)
    return grille


# def random_number(myarray, how_much_number):
#     for i in range(myarray):
#         myarray = myarray[i] * np.random.random_sample(how_much_number)
#     return myarray


# sudoku_grille = create_grille(9, 9)

# print(sudoku_grille)


# print(random_number(sudoku_grille, 10))


# create the conditions

class SudokuGrille:


    def __init__(self, nblignes, nbcolonnes):
        self.nblignes = nblignes
        self.nbcolonnes = nbcolonnes


    def create_a_grille(self, nblignes, nbcolonnes):
        grille = [[]] * nblignes
        for i in range(nblignes):
            grille[i] = [0] * nbcolonnes
        grille = np.array(grille)
        return grille


grille = SudokuGrille(9, 9)
print(grille)
