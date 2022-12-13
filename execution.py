import to_list
import checker_list
import checker_numpy
import solver
import Visuel
import creator
import numpy as np

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


#print(checker_list.sudoku_check(grille_valide_non_remplie))

#my_array = np.array(grille_valide_non_remplie)
#print(checker_numpy.sudoku_check(my_array))

#print(solver.solver(grille_valide_non_remplie))

#print(Visuel.init_grid(creator.creator_sudoku("hard")))

# Visuel.init_grid(grille_valide_non_remplie)



# On importe la librairie time pour voir le temps d'execution
import time
start_time = time.time()
# entrer la fonction ci_dessous :

end_time = time.time()
total_time = end_time - start_time
print("Time: ", total_time)
