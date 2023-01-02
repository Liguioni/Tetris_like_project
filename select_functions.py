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


def choose_piece(playable_pieces):
    piece_choice = input("Choisissez une pièce :")
    if piece_choice != "quitter":
        while int(piece_choice) not in list(playable_pieces.keys()) or len(piece_choice) > 2:
            print()
            piece_choice = input("Choisissez une pièce :")
    return piece_choice


def choose_piece_coordinates():
    line = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    column = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    piece_coordinates_choice = input("Choisissez son emplacement :")
    while len(piece_coordinates_choice) != 2 or piece_coordinates_choice[0] not in line or piece_coordinates_choice[1] not in column:
        print()
        piece_coordinates_choice = input("Choisissez son emplacement :")
    piece_coordinates = modify_functions.attribute_coordinates_to_linecolumns(piece_coordinates_choice)
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
