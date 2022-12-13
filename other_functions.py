def change_character(board):
    liste = []
    for line in board:
        column = []
        for character in line:
            column.append(character)
        liste.append(column)
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == "0":
                liste[i][j] = " "
            if liste[i][j] == "1":
                liste[i][j] = "."
            if liste[i][j] == "2":
                liste[i][j - 1] = "["
                liste[i][j] = " "
                liste[i][j + 1] = "]"
    return liste


def transform_board_into_matrice(board):
    liste = []
    with open("Boards/" + board + ".txt", "r") as matrice:
        line = matrice.readline()
        while line != "":
            liste.append(line[:-1])
            line = matrice.readline()
    return liste


def transform_pieces_to_matrice(board):
    with open("Pieces/common_pieces.txt", "r") as common_pieces:
        contenu1 = common_pieces.read()
    with open("Pieces/" + board + "_pieces.txt", "r") as special_pieces:
        contenu2 = special_pieces.read()
    common_pieces = contenu1.split("\n")
    special_pieces= contenu2.split(("\n"))
    playable_pieces = common_pieces + special_pieces
    return playable_pieces


def transfer_pieces_to_dictionary(board):
    playable_pieces = {}
    matrice_playable_pieces = transform_pieces_to_matrice(board)
    liste = []
    i = 1
    for line in matrice_playable_pieces:
        if len(line) == 10:
            liste.append(line[:-1])
            playable_pieces[i] = liste
            liste = []
            i += 1
        else:
            liste.append(line)
    return playable_pieces
