import display_functions
import modify_functions
import navigate_functions
import select_functions
import time


def verify(board, piece, piece_coordinates, playable_pieces, life, score):
    import time
    i, j, k, l = 27, 3, 4, 1
    verification = True
    while i != piece_coordinates[0]:
        i -= 1
    while j != piece_coordinates[1]:
        j += 3
    while verification is True and k >= 0:
        while verification is True and l <= 13:
            if (j > (len(board[1])-3) or j < 3) or (i > (len(board)-3) or i < 2):
                if int(playable_pieces[int(piece)][k][l]) == 0:
                    j += 3
                    l += 3
                else:
                    life -= 1
                    verification = False
                    print("Emplacement non-valide")
                    time.sleep(2)
            else:
                if (int(board[i][j]) != 1) and (int(playable_pieces[int(piece)][k][l]) == 1):
                    life -= 1
                    verification = False
                    print("Emplacement non-valide")
                    time.sleep(2)
                else:
                    board[i] = board[i][:j] + str(int(board[i][j]) + int(playable_pieces[int(piece)][k][l])) + board[i][j + 1:]
                    j += 3
                    l += 3
        j -= 3 * 5
        i -= 1
        k -= 1
        l = 1
    if verification is True:
        score += 100
    maj = [board, life, score]
    return maj


def list_columns_deletable(board):
    delete = True
    liste_columns = []
    i = 2
    for j in range(3, len(board[1])-2, 3):
        while i <= (len(board)-3) and delete is True:
            if int(board[i][j]) == 1:
                delete = False
            else:
                i += 1
        i = 2
        if delete is True:
            liste_columns.append(j)
        delete = True
    return liste_columns


def list_lines_deletable(board):
    delete = True
    liste_lines = []
    j = 3
    for i in range(2, len(board)-3):
        while j <= len(board[1])-2 and delete is True:
            if int(board[i][j]) == 1:
                delete = False
            else:
                j += 3
        j = 3
        if delete is True:
            liste_lines.append(i)
        delete = True
    return liste_lines


def gravity(board, lines_deleted):
    for line in lines_deleted:
        coordinates_liste = []
        for j in range(3, len(board[1])-2, 3):
            i = 1
            while (line - i) >= 2 and board[line - i][j] != 2:
                i += 1
            if (line - i) >= 2:
                coordinates_liste.append([line - i, j])
        mini = 30
        for coordinates in coordinates_liste:
            k = 1
            while ((coordinates[0]-k) <= (len(board)-4)) and (int(board[coordinates[0]-k][coordinates[1]]) == 1):
                k += 1
            if mini > k:
                mini = k
        for j in range(3, len(board[1])-2, 3):
            for i in range(line-1, 1, -1):
                p = 1
                while (board[i+p][j] != 0) and (p <= mini):
                    p += 1
                board[i+p-1] = board[i+p-1][:j] + board[i][j] + board[i+p-1][j+1:]
                board[i] = board[i][:j] + "1" + board[i][j+1]


def delete_line_column(board, score, life):
    liste_columns = list_columns_deletable(board)
    liste_lines = list_lines_deletable(board)
    for line in liste_lines:
        for j in range(3, len(board[1])-2, 3):
            if int(board[line][j]) == 2:
                board[line] = board[line][:j] + "1" + board[line][j + 1:]
    for column in liste_columns:
        for i in range(2, len(board)-1):
            if int(board[i][column]) == 2:
                board[i] = board[i][:column] + "1" + board[i][column + 1:]
    maj_score = score + (1000 * (len(liste_columns) + len(liste_lines)))
    display_functions.display_game3(life, maj_score, board)
 #   if len(liste_lines) != 0:
 #       gravity(board, liste_lines)
 #       display_functions.display_game3(life, maj_score, board)
 #       maj = [board, maj_score]
 #   else:
    display_functions.display_game3(life, maj_score, board)
    maj = [board, maj_score]
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
            piece_coordinates = select_functions.choose_piece_coordinates(board)
            maj = verify(board, piece_choice, piece_coordinates, playable_pieces, life, score)
            while maj[1] != life and maj[1] != 0:
                life = maj[1]
                display_functions.display_game2(life, score, board, playable_pieces, piece_choice)
                piece_coordinates = select_functions.choose_piece_coordinates(board)
                maj = verify(board, piece_choice, piece_coordinates, playable_pieces, life, score)
            board = maj[0]
            life = maj[1]
            score = maj[2]
        if life == 0:
            print("\n"*30)
            print("Game Over")
            time.sleep(2)
            print("\n"*30)
            print("Score :", score)
            time.sleep(4)
            navigate_functions.navigate_welcome()
        else:
            maj = delete_line_column(board, score, life)
            board = maj[0]
            score = maj[1]
