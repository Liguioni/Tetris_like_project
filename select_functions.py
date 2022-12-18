import display_functions
import modify_functions


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


def choose_piece_coordinates(board):
    piece_coordinates = modify_functions.attribute_coordinates_to_linecolumns(input("Choisissez son emplacement :"))
    while len(board)-2 < piece_coordinates[0] < 2 or len(board[1])-6 < piece_coordinates[1] < 3:
        print()
        piece_coordinates = modify_functions.attribute_coordinates_to_linecolumns(input("Choisissez son emplacement :"))
    return piece_coordinates


def select_playable_pieces(board):
    playable_pieces = modify_functions.transfer_pieces_to_dictionary(board)
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