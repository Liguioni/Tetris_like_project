import display_functions
import modify_functions
import navigate_functions
import select_functions
import time


def verify(board, piece, piece_coordinates, playable_pieces, life, score):
    import time
    line = piece_coordinates[0]
    column = piece_coordinates[1]
    i, j = -1, 1
    verification = True
    while verification is True and i >= -5:
        while verification is True and j <= 13:
            if (2 > line > (len(board) - 2)) or (1 > column > len(board[1]) - 3):
                if int(playable_pieces[int(piece)][i][j]) == 1:
                    verification = False
                    life -= 1
                    print("Emplacement non-valide")
                    time.sleep(2)
            else:
                if (int(playable_pieces[int(piece)][i][j]) == 1) and (int(board[line][column]) == 0):
                    verification = False
                    life -= 1
                    print("Emplacement non-valide")
                    time.sleep(2)
                elif (int(playable_pieces[int(piece)][i][j]) == 1) and (int(board[line][column]) == 2):
                    verification = False
                    life -= 1
                    print("Emplacement non-valide")
                    time.sleep(2)
            column += 3
            j += 3
        column = piece_coordinates[1]
        line -= 1
        j -= 15
        i -= 1
    if verification is True:
        modify_functions.put_piece_on_board(board, piece_coordinates, piece, playable_pieces)
        score += 100
    maj = [life, score]
    return maj


def list_deletable_columns(board):
    delete = True
    liste_columns = []
    i = 2
    for j in range(3, len(board[1])-2, 3):
        while i <= (len(board)-2) and delete is True:
            if int(board[i][j]) == 1:
                delete = False
            i += 1
        if delete is True:
            liste_columns.append(j)
        i = 2
        delete = True
    return liste_columns


def list_deletable_lines(board):
    delete = True
    liste_lines = []
    j = 3
    for i in range(2, len(board)-1):
        while j <= (len(board[1])-3) and delete is True:
            if int(board[i][j]) == 1:
                delete = False
            j += 3
        if delete is True:
            liste_lines.append(i)
        j = 3
        delete = True
    return liste_lines


def gravity_check(board, coordinates):
    gravity_liste = []
    i = 0
    for j in range(3, 79, 3):
        if coordinates[i] != 0 and board[coordinates[i] + 1][j] == "2":
            gravity_liste.append(False)
        elif coordinates[i] != 0 and board[coordinates[i] + 1][j] == "1":
            gravity_liste.append(True)
        elif coordinates[i] != 0 and board[coordinates[i] + 1][j] not in ("1", "2"):
            gravity_liste.append("Stop")
        else:
            gravity_liste.append("Unnecessary")
        i += 1
    return gravity_liste


def gravity(board, life, score, lines_deleted):
    for line in lines_deleted:
        if "2" not in board[line]:
            coordinates = []
            for k in range(3, 79, 3):
                if board[line][k] != "0":
                    l = 1
                    while line - l >= 2 and board[line - l][k] != "2":
                        l += 1
                    if line - l >= 2:
                        coordinates.append(line - l)
                    else:
                        coordinates.append(0)
                else:
                    coordinates.append(0)
            gravity_liste = gravity_check(board, coordinates)
            while False not in gravity_liste and True in gravity_liste:
                m = 0
                j = 3
                for possibility in gravity_liste:
                    if possibility not in ("Stop", "Unnecessary"):
                        line = coordinates[m]
                        for k in range(line, 1, -1):
                            if k + 1 <= 27 and board[k][j] != "0":
                                board[k + 1] = board[k + 1][:j] + board[k][j] + board[k + 1][j + 1:]
                                board[k] = board[k][:j] + "1" + board[k][j + 1:]
                        if line + 1 <= 27:
                            coordinates[m] += 1
                        else:
                            coordinates[m] = 27
                    m += 1
                    j += 3
                display_functions.display_game3(life, score, board)
                time.sleep(0.5)
                gravity_liste = gravity_check(board, coordinates)


def delete_line_column(board, score, life):
    liste_columns = list_deletable_columns(board)
    liste_lines = list_deletable_lines(board)
    while len(liste_lines) != 0 or len(liste_columns) != 0:
        for line in liste_lines:
            for j in range(3, len(board[1])-2, 3):
                if int(board[line][j]) == 2:
                    board[line] = board[line][:j] + "1" + board[line][j + 1:]
        for column in liste_columns:
            for i in range(2, len(board)-1):
                if int(board[i][column]) == 2:
                    board[i] = board[i][:column] + "1" + board[i][column + 1:]
        score += (1000 * (len(liste_columns) + len(liste_lines)))
        display_functions.display_game3(life, score, board)
        time.sleep(1)
        if len(liste_lines) != 0:
            gravity(board, life, score, liste_lines)
        liste_columns = list_deletable_columns(board)
        liste_lines = list_deletable_lines(board)
    maj = score
    return maj


def play():
    initial_parameters = select_functions.choose_initial_parameters()
    playable_pieces = select_functions.select_playable_pieces(initial_parameters[0])
    board = modify_functions.transform_board_into_matrice(initial_parameters[0])
    life = 3
    score = 0
    while life > 0:
        display_functions.display_game1(life, score, board, playable_pieces, initial_parameters)
        piece_choice = select_functions.choose_piece(playable_pieces)
        if piece_choice == "quitter":
            life = 0
        else:
            display_functions.display_game2(life, score, board, playable_pieces, piece_choice)
            piece_coordinates = select_functions.choose_piece_coordinates()
            maj = verify(board, piece_choice, piece_coordinates, playable_pieces, life, score)
            while maj[0] != life and maj[0] != 0:
                life = maj[0]
                display_functions.display_game2(life, score, board, playable_pieces, piece_choice)
                piece_coordinates = select_functions.choose_piece_coordinates()
                maj = verify(board, piece_choice, piece_coordinates, playable_pieces, life, score)
            life = maj[0]
            score = maj[1]
            display_functions.display_game3(life, score, board)
            time.sleep(1)
        if life == 0:
            print("\n"*30)
            print("Game Over")
            time.sleep(1)
            print("\n"*30)
            print("Score :", score)
            time.sleep(3)
            navigate_functions.navigate_welcome()
        else:
            maj = delete_line_column(board, score, life)
            if maj != score:
                score = maj
