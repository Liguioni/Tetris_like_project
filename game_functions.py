import display_functions
import other_functions


def choose_board():
    display_functions.display_3_boards()
    board = ""
    choice = 0
    while choice not in (1, 2, 3):
        print("")
        print("Appuyez sur 1 pour sélectionner le plateau en losange.")
        print("Appuyez sur 2 pour sélectionner le plateau en cercle.")
        print("Appuyez sur 3 pour sélectionner le plateau en triangle.")
        print()
        choice = int(input(">>>"))
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


def select_playable_pieces(board):
    playable_pieces = other_functions.transfer_pieces_to_dictionary(board)
    return playable_pieces


#def select_3_random_pieces(playable_pieces):
#    import random
#    ChosenPiece = []
#    DicoTemp = playable_pieces.copy()
#    for i in range(3):
#        B = random.randint(1, len(DicoTemp.keys()))
#        ChosenPiece.append(B)
#        DicoTemp.pop(B, None)
#    return ChosenPiece


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


def verify(board, piece, piece_coordinates):
    for i in range(27, 1, -1):
        if i ==
            for j in range(3, len(board)-3, 3):



def choose_initial_parameters():
    parameters = (choose_board(), choose_game_mode())
    return parameters


def play():
    initial_parameters = choose_initial_parameters()
    playable_pieces = select_playable_pieces(initial_parameters[0])
    board = other_functions.transform_board_into_matrice(initial_parameters[0])
    life = 3
    score = 0
    while life > 0 or piece_choice != "quitter":
        display_functions.display_game(life, score, board, playable_pieces, initial_parameters)
        piece_choice = input("Choisissez une pièce :")
        while len(playable_pieces.keys()) < piece_choice < 1:
            piece_choice = input("Choisissez une pièce :")
        print()
        piece_coordinates = input("Choisissez son emplacement :")
        verify(board, piece_choice, piece_coordinates)

#    with open("Boards/" + board + ".txt", 'r'):
#
#        while life != 0:
#            choose_position(piece)
#            verify_position(life)
#
#    display_grid()
