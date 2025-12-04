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
import pygame.gfxdraw


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
                pygame.gfxdraw.filled_circle(screen, ((x*40)+40), ((y*40)+40), 10, (120, 120, 120))
                pygame.gfxdraw.aacircle(screen, ((x*40)+40), ((y*40)+40), 10, (120, 120, 120))
            if g[x][y] == 1:
                pygame.gfxdraw.filled_circle(screen, ((x*40)+40), ((y*40)+40), 19, (240, 240, 240))
                pygame.gfxdraw.aacircle(screen, ((x*40)+40), ((y*40)+40), 19, (240, 240, 240))
            elif g[x][y] == 2:
                pygame.gfxdraw.filled_circle(screen, ((x*40)+40), ((y*40)+40), 19, (23, 22, 22))
                pygame.gfxdraw.aacircle(screen, ((x*40)+40), ((y*40)+40), 19, (23, 22, 22))

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


pygame.init()
screen = pygame.display.set_mode(size= (1400, 800))
running = True
clock = pygame.time.Clock()
joueur = 0
BLUE = (0, 0, 255)
a, b = 0, 0
pygame.font.init()
font = pygame.font.SysFont("calibri", 35)
render = True
gr = grille()
gril = gr
couleurjoueur = ["blancs", "noirs"]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = (event.pos[0]+19)//40
            b = (event.pos[1]+19)//40
            print(event.pos[0], a)
            print(event.pos[1], b)
            if verif(a, b, gr) == True:
                gril = joue(a, b, gr, joueur)
                affichage_graph(gril)
                if gagner(a, b, gril, joueur) == True:
                    texte = font.render(f"Les {couleurjoueur[joueur%2]} ont gagné", True, (0, 0, 0))
                    pygame.draw.rect(screen, (217, 186, 108), (800, 20, 1400, 100))
                    screen.blit(texte, (820, 40))
                    print(f"Le joueur {joueur%2+1} à gagné")
                    pygame.display.flip()
                    render = False
                else:
                    joueur += 1
                    gr = gril
            elif verif(a, b, gril) == False:
                print("T'es bête ou quoi mon frr")
    screen.fill((217, 186, 108))
    affichage_graph(gr)
    if render == True:
        texte = font.render(f"C'est aux {couleurjoueur[joueur%2]} de jouer", True, (0, 0, 0))
        screen.blit(texte, (820, 40))
        pygame.display.flip()
    clock.tick(60)

pygame.quit()
