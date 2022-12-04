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
        if len(set(grille[row_nb])) == 9 and 0 not in grille:
            print(f"The row {row_nb+1} is OK !")
            print(grille[row_nb])

        else:
            print(f"The row {row_nb} is not OK")
            print(grille[row_nb])

    return print("Voici votre Sudoku:\n ", np.array(grille))

# test de la fonction row_check

# print(row_check(sudoku_1))
# print(row_check(grid1))


# définir la fonction qui vérifie la colonne

def col_check(grille):

    col_nb = 0

    for col_nb in range(0, 9):
        col = [index[col_nb] for index in grille]
        if len(set(col)) == 9 and 0 not in grille:
            print(f"the column {col_nb+1} is OK !")
            print(col)
        else:
            print(f"the column {col_nb+1} is not OK")
            print(col)

    return print("Voici votre Sudoku:\n ", np.array(grille))

# test de la fonction col_check

# print(col_check(sudoku_1))
# print(col_check(grid1))

# definir la fonction qui vérifie les blocs 3*3

def bloc_check(grille):

    num_bloc = 0
    cel_row = 0
    cel_col = 0

    for cel_row in range(0, 9, 3):
        for cel_col in range(0, 9, 3):
            bloc = grille[cel_row][cel_row: cel_row+3]
            bloc.extend(grille[cel_row+1][cel_col: cel_col+3])
            bloc.extend(grille[cel_row+2][cel_col: cel_col+3])
            num_bloc += 1

            if len(set(bloc)) == 9 and 0 not in grille:
                print(f"Le bloc numéro {num_bloc} est valide !!")
                print(bloc)

            else :
                print(f"Le bloc numéro {num_bloc} n'est pas valide !!")
                print(bloc)

    return print("Voici votre Sudoku:\n ", np.array(grille))

# test de la fonction qui vérifie la cellule

# print(bloc_check(sudoku_1))
# print(bloc_check(grid1))


# définir la fonction qui vérifie toutes les lignes, colonnes et cellules 3*3

def sudoku_checker(grille):

    if row_check(grille):
        print(row_check(grille))

    if col_check(grille):
        print(col_check(grille))

    if bloc_check(grille):
        print(bloc_check(grille))

    final = print("Le Sudoku a fini d'être vérifié !!")
    return final

sudoku_checker(sudoku_1)
