
#fonction pour initié la grille sur pygame
def init_grid(grille):

    import pygame

    '''les paramétre de la fenetre:
whidth = taille en pixel
les couleurs sont  définies en RVB sous la forme d’un tuple de trois entiers représentant l’une des couleur rouge, vert et bleu.
'''
    WIDTH = 550
    HEIGHT = 550
    background_color = (255, 255, 255)
    background_color2 = (206, 206, 206, 100)
    trait = (0, 0,0)
    grid_color = (0, 0, 0)

    #initialize all imported pygame modules
    pygame.init()
    # crée une fenetre de taille 550 pixel par 550 pixel
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    # titre à la fenetre
    pygame.display.set_caption("Sudoku-lover")
    # remplir avec la couleur choisi
    window.fill(background_color)
    # taille et font des chiffres
    myfont = pygame.font.SysFont('Arial', 35)

    grid= grille

    '''Realisation d'une customisation de la grille'''
    # permet de realisé un carré de taille 150 par 150
    surface = pygame.Surface((150, 150))
    #colorie le carré former en gris ( un peu transparant)
    surface.fill(background_color2)
    # place 5 carré sur le background
    window.blit(surface, (50, 50))
    window.blit(surface, (50, 350))
    window.blit(surface, (350, 50))
    window.blit(surface, (350, 350))
    window.blit(surface, (200, 200))
    # display.flip() permet une update d'une partie de la  fenetre pour faire apparaitre les carrées gris
    pygame.display.flip()

    '''Dessine la grille '''
    for i in range(0,10):
        #dessiné la ligne verticale avecc draw.line en parrametre la fenetre choisi, la couleur du trait et la position sur la grille (debut)(fin) et enfin l'epaisseur. ( premier trait sera a 50+50*0,50 et 50+50*0,500)
        pygame.draw.line(window,trait, (50 + 50*i, 50), (50 + 50*i ,500 ), 3 )
        #ligne horizontal
        pygame.draw.line(window,trait, (50, 50 + 50*i), (500, 50 + 50*i), 3 )
    pygame.display.update()

    ''' Ecrire les chiffres sur la grille '''
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                #draw text on a new Surface  render(text, antialias(ecriture lisse), color, background=None) -> Surface
                value = myfont.render(str(grid[i][j]), True, grid_color)
                window.blit(value, ((j+1)*50 + 15, (i+1.15)*50 ))
    pygame.display.update()


    '''pour fermer la fenetre si on appuye sur la croix.'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(window, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
