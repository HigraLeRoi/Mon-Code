#=====================================#
#=== Code réalisé par Jean Bernard ===#
#=========== Aka Higraoid ============#
#=====================================#
#======= github.com/HigraLeRoi =======#
#=====================================#
#=============== V1.2 ================#
#==== Oui, je sais, on dit Gobelet ===#
#=====================================#

import random
t = [[i%2 for i in range(4)]for i in range(7)]
jouer = True
joueraléatoire = random.randint(1, 2)

while jouer == True:
    tgoblet = [0, 1, 2, 3, 4, 5, 6]
    t2 = [[]for i in range(7)]
    win = 0
    gob_suppr = 0
    nb_goblet = 7
    if joueraléatoire == 1: #le joueur 1 joue en premier
        while win == 0:
            #tour du joueur
            if nb_goblet != 0:
                goblet = int(input("Choisissezle nombre de goblets à enlever 1 et 2 \n"))
                if goblet == 1:
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 1
                elif nb_goblet >= 2:
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 2

            else:
                win = 2
                break

            print(f"Il reste {nb_goblet} goblet (après le tour du jouer 1)")
            #tour de l'ia
            if nb_goblet != 0:
                ia_remove = random.choice(t[tgoblet[0]])
                print(f"choix de l'ia {ia_remove}")
                if ia_remove == 0:
                    t2[(tgoblet[0])].append(ia_remove)
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 1    
                elif nb_goblet >= 2:
                    t2[(tgoblet[0])].append(ia_remove)
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 2
                else:
                    t2[tgoblet[0]].append(ia_remove)
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 1
            else:
                win = 1
                break
            
            print(f"Il reste {nb_goblet} goblet (après le tour de l'ia)")

    elif joueraléatoire == 2: #l'ia joue en premier
        #tour de l'ia
            if nb_goblet != 0:
                ia_remove = random.choice(t[tgoblet[0]])
                print(f"choix de l'ia {ia_remove}")
                if ia_remove == 0:
                    t2[(tgoblet[0])].append(ia_remove)
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 1    
                elif nb_goblet >= 2:
                    t2[(tgoblet[0])].append(ia_remove)
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 2
                else:
                    t2[tgoblet[0]].append(ia_remove)
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 1
            else:
                win = 1
                break
            
            print(f"Il reste {nb_goblet} goblet (après le tour de l'ia)")
        
        #tour du joueur
            if nb_goblet != 0:
                goblet = int(input("Choisissezle nombre de goblets à enlever 1 et 2 \n"))
                if goblet == 1:
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 1
                elif nb_goblet >= 2:
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    tgoblet.remove((gob_suppr))
                    gob_suppr += 1
                    nb_goblet -= 2

            else:
                win = 2
                break
        

        
    print("proba de chaque goblets")
    print(t)
    print("\n")
    print(f"c'est le joueur {win} qui a gagné ")
    print("\n")
    #ajustement des probas
    if win == 2:
        for i in range(7):
            if t2[i] != []:
                t[i].append(t2[i][0])
    elif win == 1:
        for i in range(7):
            if t2[i] != [] and t[i] != []:
                t[i].remove(t2[i][0])
    
    print("proba de chaque gobelets après ajustement")
    print(t)
    print("\n")

    encorejouer = str(input("Tu veux encore jouer (réponds par oui ou non)"))
    if encorejouer == "oui": jouer = True
    else: jouer=False
