import display_functions
import modify_functions
import select_functions


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
            if int(board[i][j]) == 0 and int(playable_pieces[int(piece)][k][l]) == 1:
                life -= 1
                verification = False
                print("Emplacement non-valide")
                time.sleep(2)
            elif int(board[i][j]) == 2 and int(playable_pieces[int(piece)][k][l]) == 1:
                life -= 1
                verification = False
                print("Emplacement non-valide")
                time.sleep(2)
            else:
                board[i] = board[i][:j] + str(int(board[i][j]) + int(playable_pieces[int(piece)][k][l])) + board[i][j+1:]
                j += 3
                l += 3
        j -= 3*5
        i -= 1
        k -= 1
        l = 1
    if verification is True:
        score += 100
    maj = [board, life, score]
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
            board = maj[0]
            life = maj[1]
            score = maj[2]
        if life == 0:
            print("Game Over")
        
