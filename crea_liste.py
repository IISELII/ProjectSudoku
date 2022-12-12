import random

def random_number():
    randomlist = random.sample(range(1, 10), 9)
    return randomlist

def shuffle(liste):
    'pour melanger une liste'
    random.shuffle(liste)
    return liste

def change_zero(rows):
    liste= rows.copy()
    for index, elem in enumerate(liste):
        if elem == 0:
            liste[index] = random.randint(1, 9)
    return liste
