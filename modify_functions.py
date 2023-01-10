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
    special_pieces = contenu2.split(("\n"))
    playable_pieces = common_pieces + special_pieces
    return playable_pieces



def transfer_pieces_to_dictionary(board):
    playable_pieces = {}
    matrice_playable_pieces = transform_pieces_to_matrice(board)
    liste = []
    i = 1
    for line in matrice_playable_pieces:
        if len(line) == 16:
            liste.append(line[:-1])
            playable_pieces[i] = liste
            liste = []
            i += 1
        else:
            liste.append(line)
    return playable_pieces


def change_character_board(board):
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


def change_character_piece(line):
    liste = ""
    for character in line:
        if character == "0":
            liste = liste + "   "
        elif character == "1":
            liste = liste + "[ ]"
    return liste


def attribute_coordinates_to_linecolumns(piece_coordinates):
    line = ord(piece_coordinates[0])
    column = ord(piece_coordinates[1])
    coordinates = [line - 63, 3 * (column - ord("a") + 1)]
    return coordinates


def put_piece_on_board(board, piece_coordinates, piece, playable_pieces):
    line = 0
    for i in range(piece_coordinates[0], piece_coordinates[0] - 6, -1):
        line -= 1
        column = -2
        if line >= -5:
            for j in range(piece_coordinates[1], piece_coordinates[1] + 14, 3):
                column += 3
                if column <= 13:
                    if playable_pieces[int(piece)][line][column] == "1":
                        board[i] = board[i][:j] + "2" + board[i][j + 1:]
