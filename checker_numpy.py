import numpy as np
import collections

sudoku_1 = [[4, 7, 0, 3, 6, 0, 2, 0, 5],
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
    # for i in range(0, 9):
    #     print(grille[i, :])
    for i in range(0, 9):
        R = grille[i, :]
        C = collections.Counter(R)
        print(collections.Counter(R))
        for w in range(1, 10):
            if C[w] == 0 or C[w] == 1:
                True
            else:
                return False

        else:
            return False

    return True


print(row_check(my_array))


def col_check(grille):
    for j in range(0, 9):
        I = grille[:, j]
        F = collections.Counter()
    # for col_number in range(0, 9):
    #     col = [index[col_number] for index in grille]
    #     if len(col) == 9:
    #         for i in range(1, 10):
    #             if col.count(i) == 0 or col.count(i) == 1:
    #                  True
    #             else:
    #                 return False

    #     else:
    #         return False


    return True


# print(col_check(my_array))


def bloc_check(grille):

    row = 0
    col = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            row = i
            col = j

            bloc = grille[row][col: col + 3]
            bloc = np.append(bloc, grille[row + 1][col: col + 3])
            bloc = np.append(bloc, grille[row + 2][col: col + 3])
            print(bloc)


    if len(bloc) == 9:
        for i in range(1, 10):
            if bloc.count(i) == 0 or bloc.count(i) == 1:
                True
            else:
                return False

    else:
        return False

    return True


# print(bloc_check(my_array))
