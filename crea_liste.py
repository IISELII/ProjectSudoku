import random

def random_number():
    'crée une liste de 9 chiffres'
    randomlist = random.sample(range(1, 10), 9)
    return randomlist

def shuffle(liste):
    'pour melanger une liste'
    random.shuffle(liste)
    return liste
