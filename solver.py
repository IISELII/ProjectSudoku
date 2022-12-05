import pygments


grid =[
        [0, 7, 9, 3, 0, 8, 0, 0, 0],
        [0, 0, 0, 1, 9, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 6, 1, 0, 5, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 9, 0],
        [9, 4, 0, 0, 0, 0, 5, 7, 0],
        [8, 9, 0, 5, 3, 6, 0, 2, 1],
        [0, 0, 0, 0, 0, 7, 0, 6, 4],
        [7, 2, 6, 9, 4, 0, 0, 5, 0]
    ]

#fonction pour initier la grille sur pygame
def init_grid(grille):


    '''les paramétre de la fenetre
whidth = taille en pixel
les couleurs sont  définies en RVB sous la forme d’un tuple de trois entiers représentant l’une des couleur rouge, vert et bleu.
'''
    WIDTH = 550
    HEIGHT = 550
    background_color = (255, 255, 255)
    background_color2 = (206, 206, 206, 100)
    trait = (0, 0,0)
    grid_color = (0, 0, 0)
    pygments.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT)) # crée une fenetre de taille 550 pixel par 550 pixel
    pygame.display.set_caption("Sudoku-lover")# titre à la fenetre
    window.fill(background_color)# remplir avec la couleur choisie
    myfont = pygame.font.SysFont('Arial', 35) # taille et font des chiffres
    grid= grille
    surf = pygame.Surface((150, 150))
    surf.fill(background_color2)
    window.blit(surf, (50, 50))
    window.blit(surf, (50, 350))
    window.blit(surf, (350, 50))
    window.blit(surf, (350, 350))
    window.blit(surf, (200, 200))
    pygame.display.flip()


    for i in range(0,10):
        #dessiner la ligne verticale avec draw.line en parametre la fenetre choisie, la couleur du trait et la position sur la grille (debut)(fin) et enfin l'epaisseur
        pygame.draw.line(window,trait, (50 + 50*i, 50), (50 + 50*i ,500 ), 3 )
        #ligne horizontal
        pygame.draw.line(window,trait, (50, 50 + 50*i), (500, 50 + 50*i), 3 )
    pygame.display.update()


    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                #draw text on a new Surface  render(text, antialias(ecriture lisse), color, background=None) -> Surface
                value = myfont.render(str(grid[i][j]), True, grid_color)
                window.blit(value, ((j+1)*50 + 15, (i+1.15)*50 ))
    pygame.display.update()



#pour quitter si on appuye sur la croix.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(window, (pos[0]//50, pos[1]//50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return

init_grid(grid)

def is_possible_row(grid,number,x):
    for i in range (0,9) :
        if grid[x][i]==number : return False
    return True

def is_possible_column(grid,number,y):
    for i in range (0,9) :
        if grid[i][y]==number : return False
    return True

def block(x,y) :
    X=x//3
    Y=y//3
    return X,Y

def is_possible_block(grid,number,x,y) :
    X,Y=block(x,y)
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[X*3+i][Y*3+j]==number : 
                return False
    return True

def is_possible(grid,number,x,y) :
    return is_possible_row(grid,number,x) and is_possible_column(grid,number,y) and is_possible_block(grid,number,x,y)

def solver(grid):
    for x in range(0,9) :
        for y in range(0,9):
            if grid[x][y]==0 :
                for number in range(1,10):
                    if is_possible(grid,number,x,y) :
                        grid[x][y]=number
                        solver(grid)
                        grid[x][y]=0
                return
            else :
                if x==8 and y==8:
                    print(grid)
                    return   

solver(grid)