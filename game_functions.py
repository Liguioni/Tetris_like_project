import display_functions
import other_functions


def choose_board():
    print("\n" * 20)
    display_functions.display_3_boards()
    board = ""
    choice = 0
    while choice not in (1, 2, 3):
        print()
        print("Appuyez sur 1 pour sélectionner le plateau en losange.")
        print("Appuyez sur 2 pour sélectionner le plateau en cercle.")
        print("Appuyez sur 3 pour sélectionner le plateau en triangle.")
        print()
        choice = int(input(">>"))
    if choice == 1:
        board = "diamond"
    elif choice == 2:
        board = "circle"
    elif choice == 3:
        board = "triangle"
    return board


def choose_game_mode():
    print("Mode Zen : 1")
    print("Mode Défi : 2")
    print()
    choice = int(input("Choisissez votre mode de jeu :"))
    while choice not in (1, 2):
        choice = int(input("Choisissez votre mode de jeu :"))
    if choice == 1:
        choice = "Zen"
    else:
        choice == "Défi"
    return choice


def choose_initial_parameters():
    parameters = (choose_board(), choose_game_mode())
    return parameters


def select_playable_pieces(board):
    playable_pieces = other_functions.transfer_pieces_to_dictionary(board)
    return playable_pieces


def select_3_random_piece_keys(playable_pieces):
    import random
    liste = []
    keys = list(playable_pieces.keys())
    for i in range(3):
        piece = random.choice(keys)
        liste.append(piece)
        j = 0
        while piece != keys[j] or j == len(keys):
            j += 1
        del keys[j]
    return liste


def verify(board, piece, piece_coordinates, playable_pieces, life, score):
    i = 27
    j = 3
    k = 4
    l = 1
    verification = True
    while i != piece_coordinates[0]:
        i -= 1
    while j != piece_coordinates[1]:
        j += 3
    while verification is True and k >= 0:
        while verification is True and l <= 13:
            if board == 0 and playable_pieces[piece][k][l] == 1:
                life -= 1
                verification = False
                print("Emplacement non-valide")
            elif board == 2 and playable_pieces[piece][k][l] == 1:
                life -= 1
                verification = False
                print("Emplacement non-valide")
            else:
                board[i][j] = str(int(board[i][j]) + int(playable_pieces[piece][k][l]))
            j += 3
            l += 3
        j = j - (3*5)
        i -= 1
        k -= 1
    if verification is True:
        score += 100
    maj = [board, life, score]
    return maj


def play():
    initial_parameters = choose_initial_parameters()
    playable_pieces = select_playable_pieces(initial_parameters[0])
    board = other_functions.transform_board_into_matrice(initial_parameters[0])
    life = 3
    score = 0
    while life > 0:
        display_functions.display_game1(life, score, board, playable_pieces, initial_parameters)
        piece_choice = display_functions.display_piece_choice(playable_pieces)
        if piece_choice == "quitter":
            life = 0
        else:
            display_functions.display_game2(life, score, board, playable_pieces, piece_choice)
            piece_coordinates = display_functions.display_piece_coordinates(board)
            maj = verify(board, piece_choice, piece_coordinates, playable_pieces, life, score)
            board = maj[0]
            life = maj[1]
            score = maj[2]
