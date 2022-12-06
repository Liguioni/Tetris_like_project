import display_functions
import other_functions


def choose_board():
    display_functions.display_3_boards()
    board = ""
    choice = 0
    while choice == 0:
        print("")
        print("Appuyez sur 1 pour sélectionner le plateau en losange.")
        print("Appuyez sur 2 pour sélectionner le plateau en cercle.")
        print("Appuyez sur 3 pour sélectionner le plateau en triangle.")
        print("")
        choice = int(input(">>"))
        if choice != 1:
            if choice != 2:
                if choice != 3:
                    choice = 0
    if choice == 1:
        board = "diamond"
    elif choice == 2:
        board = "circle"
    elif choice == 3:
        board = "triangle"
    return board


def select_playable_pieces(board):
    playable_pieces = []
    with open("Pieces/common_pieces.txt", 'r') as common_pieces:
        line = common_pieces.readline()
        while line != "":
            playable_pieces.append(line[:-1])
            line = common_pieces.readline()
    with open("Pieces/" + board + "_pieces.txt", 'r') as special_pieces:
        line = special_pieces.readline()
        while line != "":
            playable_pieces.append(line[:-1])
            line = special_pieces.readline()
    return playable_pieces


def verify(num_life):
    num_life


def play():
    board = choose_board()
    playable_pieces = select_playable_pieces(board)
    grid = other_functions.transform_board_into_matrice(board)
    life = 3
    choice = 0
    while life > 0 or choice == "quitter":
        display_functions.display_life(life)
        display_functions.display_grid(other_functions.change_character(grid))
        choice = input("Choisissez l'emplacement de la pièce : ")

#    with open("Boards/" + board + ".txt", 'r'):
#
#        while life != 0:
#            choose_position(piece)
#            verify_position(life)
#
#    display_grid()
