import numpy as np

sudoku_1 = [[4, 7, 9, 3, 6, 8, 2, 1, 5],
            [6, 3, 2, 1, 9, 5, 4, 8, 7],
            [1, 8, 5, 2, 7, 4, 6, 3, 9],
            [3, 6, 1, 7, 5, 9, 8, 4, 2],
            [2, 5, 7, 4, 8, 3, 1, 9, 6],
            [9, 4, 8, 6, 1, 2, 5, 7, 3],
            [8, 9, 4, 5, 3, 6, 7, 2, 1],
            [5, 1, 3, 8, 2, 7, 9, 6, 4],
            [7, 2, 6, 9, 4, 1, 3, 5, 8]]

def to_array(grille):
    grille_array = np.array(grille)
    return grille_array

my_array = to_array(sudoku_1)

def row_check(grille):
    for i in range(0, 9):
        for w in range(1, 10):
            if len(set(grille[i, :])) != 9:
                return False

    return True

def col_check(grille):
    for j in range(0, 9):
        for w in range(1, 10):
            if len(set(grille[:, j])) != 9:
                return False

    return True

def block_check(grille):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            row = i
            col = j

            bloc = grille[row][col: col + 3]
            bloc = np.append(bloc, grille[row + 1][col: col + 3])
            bloc = np.append(bloc, grille[row + 2][col: col + 3])

            for w in range(1, 10):
                if len(set(bloc)) != 9:
                    return False

    return True

def sudoku_check(grille):
    return row_check(grille) and col_check(grille) and block_check(grille)


sudoku_check(my_array)

import time
start_time = time.time()
sudoku_check(my_array)
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)
