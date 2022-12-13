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

def verify(num_life):
    num_life

def RandPieceDefi(playable_pieces):       #Là j'ai pris 3 keys aléatoire et il faut maintenant afficher à un endroit les 3 pièces choisi. Incruster dans le prog une fonction display
    import random                                                   #Je sais pas pourquoi mais je peux pas essayer la fonction donc je sais pas si elle marche
    ChosenPiece = []
    ListeModi = playable_pieces.copy()
    for i in range(3):
        B = random.randint(0, (len(ListeModi)-1))
        ChosenPiece.append(ListeModi[B])
        del ListeModi[B]
    return ChosenPiece


#def calculate_score():


def play():
    board = choose_board()
    playable_pieces = select_playable_pieces(board)
    game_mode = choose_game_mode()
    grid = other_functions.transform_board_into_matrice(board)
    life = 3
    choice = 0
    score = 0
    print(playable_pieces)
    while life > 0 or choice != "quitter":
        print()
        display_functions.display_life(life)
        print()
        display_functions.display_score(score)
        print()
        display_functions.display_grid(other_functions.change_character(grid))
        print()
        display_functions.display_pieces(game_mode, playable_pieces)
        print()
        choice = input("Choisissez une pièce :")


#    with open("Boards/" + board + ".txt", 'r'):
#
#        while life != 0:
#            choose_position(piece)
#            verify_position(life)
#
#    display_grid()
