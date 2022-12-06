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