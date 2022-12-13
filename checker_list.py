# créer des grilles de sudoku à utiliser sur le checker

#  créer la grille non valide

grille_non_valide =  [
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

# créer la grille valide et remplie

sudoku_1 = [[4, 7, 9, 3, 6, 8, 2, 1, 5],
            [6, 3, 2, 1, 9, 5, 4, 8, 7],
            [1, 8, 5, 2, 7, 4, 6, 3, 9],
            [3, 6, 1, 7, 5, 9, 8, 4, 2],
            [2, 5, 7, 4, 8, 3, 1, 9, 6],
            [9, 4, 8, 6, 1, 2, 5, 7, 3],
            [8, 9, 4, 5, 3, 6, 7, 2, 1],
            [5, 1, 3, 8, 2, 7, 9, 6, 4],
            [7, 2, 6, 9, 4, 1, 3, 5, 8]]

# la grille pas finie mais valide

grille_valide_non_remplie = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]]


grid_valide = []

# On définie la fonction row_check qui va vérifier que
# toutes les lignes du sudoku ne contiennes pas de doublons

def row_check(grille):

    # boucle for qui va passer sur les 9 lignes du dataset
    for row_nb in range(0, 9):

            # boucle for où i prend les valeurs de 1 à 9 à chaque ligne
            for i in range(1, 10):

                # i va boucler 9 fois avec une valeur s'incrémentant de 1 à 9
                # en utilisant count(i) on vérifie qu'il n'y a pas de doublon
                # sur la ligne en question
                # sinon on retourne False
                if grille[row_nb].count(i) > 1:
                    return False

    # si toutes les lignes sont validé, on retourne True
    return True


# définir la fonction col_check qui va vérifier que
# toutes les lignes du sudoku ne contiennes pas de doublons

def col_check(grille):

    # boucle for où col_nb prend les valeurs 0 à 9
    for col_nb in range(0, 9):

        # col prend en index col_nb et parcours la colonne de col_nb
        col = [index[col_nb] for index in grille]

        # boucle for où i prend les valeurs de 1 à 9
        for i in range(1, 10):

            # i va boucler 9 fois avec une valeur s'incrémentant de 1 à 9
            # en utilisant count(i) on vérifie qu'il n'y a pas de doublon
            # sur la colonne en question
            # sinon on retourne False
            if col.count(i) > 1:
                return False

    # si toutes les conditions sont validés
    return True

# la fonction find_block qui définie les block
# et les stock dans la variable l1 sous forme de list de list
def find_block(grille) :

    # on créer une liste l1 vide
    l1=[]

    # X et Y définissent les 9 blocs du sudoku : (0, 0);(0, 1);(0, 2)
                                                #(1, 0);(1, 1);(1, 2)
                                                #(2, 0);(2, 1);(2, 2)
    for X in range(0,3) :
        for Y in range (0,3) :

            # on créer la liste l2 vide
            l2=[]

            # les boucles de x et y représentent pour chaque blocs leurs 9 cellules respectives
            for x in range (0,3) :
                for y in range (0,3) :

                    # on ajoute à l2 la valeur des 9 cellules du bloc
                    l2.append(grille[X * 3+x][Y * 3+y])

            # la liste l2 est ajouter à la liste vide l1, qui finira par avoir
            # les 9 block en liste de liste
            l1.append(l2)

    # On retourne l1
    return l1

# la fonction checker qui vérifie que les 3 conditions sont remplie
# pour que le sudoku soit valide

def sudoku_check(grille):
    return row_check(grille) and row_check(find_block(grille)) and col_check(grille)


# On importe la librairie time pour voir le temps d'execution de notre checker

import time
start_time = time.time()
sudoku_check(sudoku_1)
end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)
