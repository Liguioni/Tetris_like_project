# Affichage plateaux

#with open("Boards/boards.txt", 'w') as plateaux:
#    losange = open("Boards/diamond.txt", 'r')
#    L = losange.readlines()
#    losange.close()
#    cercle = open("Boards/circle.txt", 'r')
#    C = cercle.readlines()
#    cercle.close()
#    triangle = open("Boards/triangle.txt", 'r')
#    T = triangle.readlines()
#    triangle.close()
#    plateaux = open("Boards/boards.txt", 'w')
#    for i in range(0, 29):
#        plateaux.write(L[i][:-1] + "          " + C[i][:-1] + "          " + T[i])
#    plateaux.close()

########
#import display_functions


#life = 3


#while life > 0:
#    display_functions.display_life(life)
#    life -= 1


#def grid():
#    liste = []
#    with open("Boards/circle.txt", "r") as matrice:
#        line = matrice.readline()
#        while line != "":
#            liste.append(line[:-1])
#            line = matrice.readline()
#    return liste


#def change_character(board):
#    gride = []
#    for line in board:
#        column = []
#        for character in line:
#            column.append(character)
#        gride.append(column)
#    for i in range(len(gride)):
#        for j in range(len(gride[i])):
#            if gride[i][j] == "0":
#                gride[i][j] = " "
#            if gride[i][j] == "1":
#                gride[i][j] = "."
#            if gride[i][j] == "2":
#                gride[i][j-1] = "["
#                gride[i][j] = " "
#                gride[i][j+1] = "]"
#    return gride



#def display_grid():
#    gride = change_character(grid())
#    for i in range(len(gride)):
#        for j in range(len(gride[i])):
#            print(gride[i][j], end="")
#        print("")


#liste = ['0 1 0 1 0;', '1 0 1 1 0;', '0 1 0 1 1']
#for line in liste:
#    if line[-1] == ';':
#        print(line[:-1])
#    else :
#        print(line)

#playable_pieces = {}
#with open("Pieces/common_pieces.txt", "r") as pieces:
#    contenu = pieces.read()
#liste = contenu.split("\n")
#liste_2 = []
#i = 1
#for line in liste:
#    if len(line) == 10:
#        liste_2.append(line[:-1])
#        playable_pieces[i] = liste_2
#        liste_2 = []
#        i += 1
#    else:
#        liste_2.append(line)

playable_pieces = {1: "première pièce", 2: "deuxième pièce", 3: "troisième pièce", 4: "quatrième pièce"}


def select_3_random_key_pieces(playable_pieces):
    import random
    liste = []
    keys = list(playable_pieces.keys())
    print(keys)
    for i in range(3):
        piece = random.choice(keys)
        liste.append(piece)
        j = 0
        while piece != keys[j] or j == len(keys):
            j += 1
        del keys[j]
    print(keys)
    print(liste)

select_3_random_key_pieces(playable_pieces)
