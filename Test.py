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

#playable_pieces = {1: "première pièce", 2: "deuxième pièce", 3: "troisième pièce", 4: "quatrième pièce"}


#def select_3_random_key_pieces(playable_pieces):
#    import random
#    liste = []
#    keys = list(playable_pieces.keys())
#    print(keys)
#    for i in range(3):
#        piece = random.choice(keys)
#        liste.append(piece)
#        j = 0
#        while piece != keys[j] or j == len(keys):
#            j += 1
#        del keys[j]
#    print(keys)
#    print(liste)

piece_coordinates = "Aa"

#def attribute_coordinates_to_line_columns(piece_coordinates):
#    coordinates = [ord(piece_coordinates[0]), ord(piece_coordinates[1])]
#    coordinates = [coordinates[0] - 65 + 2, coordinates[1] - 97 + 4 + 3 * (coordinates[1] - ord("a"))]
#    return coordinates

#attribute_coordinates_to_line_columns(piece_coordinates)

piece_coordinates = [4,5] # [ligne, colonne]
#def attribute_coordinates_to_linecolumns(piece_coordinates):
#    line = ord(piece_coordinates[0])
#    column = ord(piece_coordinates[1])
#    coordinates = [line - 63, 3 * (column - ord("a") + 1)]
#    print(coordinates)

#attribute_coordinates_to_linecolumns(piece_coordinates)

# board est une liste 2D pour représentant le tableau.
# piece est une liste 2D pour une pièce quelconque de dimension 5x5

ligne = piece_coordinates[0]
colonne = piece_coordinates[1]
i = -1
j = 0

possible = True
while possible is True and i >= -5:
    while possible is True and j <= 4:
        if (1 > ligne > (len(board) - 1)) or (1 > colonne > len(board[0] - 1)):
            if piece[i][j] == 1:
                possible = False
        else:
            if (piece[i][j] == 1) and (board[ligne][colonne] == 0):
                possible = False
            elif (piece[i][j] == 1) and (board[ligne][colonne] == 2):
                possible = False
            elif (piece[i][j] == 1) and (board[ligne][colonne] == 1):
                board[ligne] = board[ligne][:colonne] + "1" + board[ligne][colonne + 1:]
        colonne += 1
        j += 1
    colonne = piece_coordinates[1]
    j -= 5
    i -= 1

# deletable_lines est une liste de valeurs correspondant aux lignes supprimables
# deletable_columns est une liste de valeurs correspondant aux colonnes supprimables


