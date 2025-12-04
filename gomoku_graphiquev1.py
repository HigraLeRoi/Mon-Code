'''
Ce jeu a été fait par higraoid, higraaaa sur discord
si il y a des bugs, merci de m'en faire part
Le but du jeu de gomoku c'est d'aligner 5 pion à la 
verticale, diagonale ou horizontale.
Au début y'a quelques règles si vous voulez vrm jouer, 
je vous laisser regarder ça sur internet
'''

import pygame
import time

def grille():
    return [[0 for i in range(19)] for j in range(19)]
#a = ligne, b=colonne

def affichage(g):
    n = len(g)
    w = len(str(n))
    symbole = {0: ".", 1: "X", 2: "O"}
    for j in range(n):
        row = [symbole[x] for x in g[n-1-j]]
        print(str(n-j).rjust(w) + " " + " ".join(s.rjust(w) for s in row))
    print(" " * (w+1) + " ".join(str(i+1).rjust(w) for i in range(n)))

def affichage_graph(g):
    for x in range(19):
        for y in range(19):
            if g[x][y] == 0:
                pygame.draw.circle(screen, (225, 225, 225), ((x*20)+20, (y*20)+20), 10)
            if g[x][y] == 1:
                pygame.draw.circle(screen, BLUE, ((x*20)+20, (y*20)+20), 10)
            elif g[x][y] == 2:
                pygame.draw.circle(screen, BLACK, ((x*20)+20, (y*20)+20), 10)

def verif(a, b, g):
    ap, bp = a-1, b-1
    if (ap<0 or ap>len(g)-1) or (bp<0 or bp>len(g)-1):
        return False
    elif g[ap][bp] == 0:
        return True
    return False

def joue(a, b, g, j):
    a = a-1
    b = b-1
    if verif(a+1, b+1, g) == True:
        g[a][b] = j%2+1
    return g

def gagner(a, b, g, j):
    nb = 0
    a, b = a-1, b-1
    for i in range(5):
        nb = 0
        for k in range(5):
            ap, bp = a-i, b-i
            try:
                if g[ap+k][bp+k] == (j%2+1):
                    nb += 1
                if nb == 5:
                    return True
            except IndexError:
                None
    for i in range(5):
        nb = 0
        for k in range(5):
            ap, bp = a-i, b-i
            try:
                if g[ap-k][bp+k] == (j%2+1):
                    nb += 1
                if nb == 5:
                    return True
            except IndexError:
                None
    for i in range(5):
        nb = 0
        for k in range(5):
            ap = a-i
            try:
                if g[ap+k][b] == (j%2+1):
                    nb += 1
                if nb == 5:
                    return True
            except IndexError:
                None
    for i in range(5):
        nb = 0
        for k in range(5):
            bp = b-i
            try:
                if g[a][bp+k] == (j%2+1):
                    nb += 1
                if nb == 5:
                    return True
            except IndexError:
                None

# fin = False
pygame.init()
screen = pygame.display.set_mode(size= (400, 400))
running = True
clock = pygame.time.Clock()
joueur = 0
gr = grille()
gril = gr
affichage(gr)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
a, b = 0, 0
pygame.font.init()
font = pygame.font.SysFont("arial", 24)
render = True
while running:
    # if joueur%2 == 0:
    #     a = int(input("Joueur 1 : ligne "))
    #     b = int(input("Joueur 1 : colonne "))
    #     if verif(a, b, gr) == True:
    #         gril = joue(a, b, gr, joueur)
    #         affichage(gril)
    #         if gagner(a, b, gril, joueur) == True:
    #             print("Le joueur 1 à gagné")
    #         else:
    #             joueur += 1
    #             gr = gril
    #     elif verif(a, b, gril) == False:
    #         print("T'es bête ou quoi mon frr")
    # elif joueur%2 == 1:
    #     a = int(input("Joueur 2 : ligne "))
    #     b = int(input("Joueur 2 : colonne "))
    #     if verif(a, b, gr) == True:
    #         gril = joue(a, b, gr, joueur)
    #         affichage(gril)
    #         if gagner(a, b, gril, joueur) == True:
    #             print("Le joueur 2 à gagné")
    #         else: 
    #             joueur += 1
    #             gr = gril
    #     elif verif(a, b, gril) == False:
    #         print("T'es bête ou quoi mon frr")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = (event.pos[0]+9)//20
            b = (event.pos[1]+9)//20
            print(event.pos[0], a)
            print(event.pos[1], b)
            if joueur%2 == 0:
                if verif(a, b, gr) == True:
                    gril = joue(a, b, gr, joueur)
                    affichage_graph(gril)
                    if gagner(a, b, gril, joueur) == True:
                        texte = font.render("Le joueur 1 à gagné", True, (0, 0, 0))
                        screen.blit(texte, (20, 20))
                        print("Le joueur 1 à gagné")
                        pygame.display.flip()
                        render = False
                    else:
                        joueur += 1
                        gr = gril
                elif verif(a, b, gril) == False:
                    print("T'es bête ou quoi mon frr")
            elif joueur%2 == 1:
                if verif(a, b, gr) == True:
                    gril = joue(a, b, gr, joueur)
                    affichage_graph(gril)
                    if gagner(a, b, gril, joueur) == True:
                        texte = font.render("Le joueur 2 à gagné", True, (0, 0, 0))
                        screen.blit(texte, (20, 20))
                        pygame.display.flip()
                        render = False
                    else: 
                        joueur += 1
                        gr = gril
                elif verif(a, b, gril) == False:
                    print("T'es bête ou quoi mon frr")
    screen.fill(WHITE)
    affichage_graph(gr)
    if render == True:
        pygame.display.flip()
    clock.tick(60)

pygame.quit()
