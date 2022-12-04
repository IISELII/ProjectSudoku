import random
import numpy as np


# def row_valid(row_number):
#     return len(set(sudoku_liste[row_number])) == 9


# def col_valid(col_num):
#     col = [index[col_num] for index in sudoku_liste]
#     return len(set(col)) == 9



# def validate_sudoku():
#     for i in range(0, 9):
#         if not row_valid:
#             return False
#         if not col_valid:
#             return False

#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             print(i, j)
#             if not is_cel_valid(i, j):
#                 return False

#     return False

# if validate_sudoku():
#     print("Le Sudoku est valide !")

# else :
#     print("Le Sudoku n'est pas valide :(")


# print(validate_sudoku(sudoku_liste))

# print(sudoku_liste)

# def validation_row(grid, row_number):
#     return len(set(grid[row_number])) == 9 and 0 not in grid[row_number]

# def validation_column(grid, column_number):
#     col = [index[column_number] for index in grid]
#     return len(set(col)) == 9 and 0 not in col

# def validation_cellule(grid, cel_row, cel_col):
#     val = grid[cel_row][cel_col: cel_col+3]
#     val.extend(grid[cel_row+1] [cel_col: cel_col+3])
#     val.extend(grid[cel_row+2] [cel_col: cel_col+3])
#     return len(set(val)) == 9 and 0 not in val

# def valide_sudoku(grid):

#     for i in range(0, 9):
#         if not validation_row:
#             return False
#         if not validation_column:
#             return False

#         for i in range(0, 9, 3):
#             for j in range(0, 9, 3):
#                 if not validation_cellule:
#                     return False

#     return False

# if valide_sudoku():
#     print("Valide !")

# else :
#     print("Non Valide !")



# print(row_valid(0))
# print(col_valid(0))
# print(is_cel_valid(1, 3))


grid =[
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

grid_valid = [
        [5, 3, 9, 8, 7, 6, 4, 1, 2],
        [7, 2, 8, 3, 1, 4, 9, 6, 5],
        [6, 4, 1, 2, 9, 5, 7, 3, 8],
        [4, 6, 2, 5, 3, 9, 8, 7, 1],
        [3, 8, 5, 7, 2, 1, 6, 4, 9],
        [1, 9, 7, 4, 6, 8, 2, 5, 3],
        [2, 5, 6, 1, 8, 7, 3, 9, 4],
        [9, 1, 3, 6, 4, 2, 5, 8, 7],
        [8, 7, 4, 9, 5, 3, 1, 2, 6]
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

# def row_check(grille):

#     for row_number in range(0, 9):
#         row = grille[row_number]
#         if len(set(row)) == 9 and 0 not in row:
#             print(row)
#             print("the check is ok !")

#         else :
#             return "colonne is not OK"

#     return print("OK LIGNE")

def col_check(grille):

    for col_number in range(0, 9):
        col = [index[col_number] for index in grille]
        if len(set(col)) == 9 and 0 not in col:
            print(col)
            print("col is ok !")

        else :
            return "colonne is not OK"

    return print("OK COLONNE")


print(col_check(sudoku_1))
# def cel_check(grille):

#     for cel_row in range(0, 9, 3):
#         for cel_col in range(0, 9, 3):
#             val = grille[cel_row][cel_col: cel_col+3]
#             val.extend(grille[cel_row+1][cel_col: cel_col+3])
#             val.extend(grille[cel_row+2][cel_col: cel_col+3])


#         if len(set(val)) == 9 and 0 not in val:
#                 print(val)
#                 print("the cell is ok !")

#     return print("OK CELL")


# def sudoku_check(grille):

#     for i in range(0, 9):

#         if not row_check(grille):
#             return False

#         elif not col_check(grille):
#             return False


#         elif not cel_check(grille):
#             return False

#         else :
#             return True







# print(row_check(grid))

# print(col_check(grid))

# print(cel_check(sudoku_1))


# print(sudoku_check(sudoku_1))
