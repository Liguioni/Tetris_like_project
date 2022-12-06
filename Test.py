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
#    total = []
#    for i in range(1, 29):
#        total.append(L[i][:-1] + "  " + C[i][:-1] + "  " + T[i])
#    plateaux = open("Boards/boards.txt", 'w')
#    for ligne in total:
#        plateaux.write(ligne)
#    plateaux.close()

########
import display_functions


life = 3


while life > 0:
    display_functions.display_life(life)
    life -= 1


def grid():
    liste = []
    with open("Boards/circle.txt", "r") as matrice:
        line = matrice.readline()
        while line != "":
            liste.append(line[:-1])
            line = matrice.readline()
    return liste


def change_character(board):
    gride = []
    for line in board:
        column = []
        for character in line:
            column.append(character)
        gride.append(column)
    for i in range(len(gride)):
        for j in range(len(gride[i])):
            if gride[i][j] == "0":
                gride[i][j] = " "
            if gride[i][j] == "1":
                gride[i][j] = "."
            if gride[i][j] == "2":
                gride[i][j-1] = "["
                gride[i][j] = " "
                gride[i][j+1] = "]"
    return gride



def display_grid():
    gride = change_character(grid())
    for i in range(len(gride)):
        for j in range(len(gride[i])):
            print(gride[i][j], end="")
        print("")



