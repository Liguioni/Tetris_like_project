import modify_functions
import game_functions


def display_grid(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j], end="")
        print("")


def display_welcome():
    with open("Menu/welcome.txt", 'r') as welcome:
        ligne = welcome.readline()
        while ligne != "":
            print(ligne[:-1])
            ligne = welcome.readline()


def display_rules():
    with open("Menu/rules.txt", 'r') as regles:
        ligne = regles.readline()
        while ligne != "":
            print(ligne[:-1])
            ligne = regles.readline()


def display_diamond():
    board = "diamond"
    matrice = modify_functions.transform_board_into_matrice(board)
    grid = modify_functions.change_character_board(matrice)
    display_grid(grid)


def display_circle():
    board = "circle"
    matrice = modify_functions.transform_board_into_matrice(board)
    grid = modify_functions.change_character_board(matrice)
    display_grid(grid)


def display_triangle():
    board = "triangle"
    matrice = modify_functions.transform_board_into_matrice(board)
    grid = modify_functions.change_character_board(matrice)
    display_grid(grid)


def display_3_boards():
    with open("Boards/diamond.txt", 'r') as diamond:
        L = diamond.readlines()
        diamond.close()
    with open("Boards/circle.txt", 'r') as circle:
        C = circle.readlines()
        circle.close()
    with open("Boards/triangle.txt", 'r') as triangle:
        T = triangle.readlines()
        triangle.close()
    board = []
    for i in range(0, 29):
        if i <= 15:
            line = L[i][:-1] + "     " + C[i][:-1] + "     " + T[i][:-1]
            board.append(line)
        else:
            line = L[i][:-1] + "     " + C[i][:-1]
            board.append(line)
    grid = modify_functions.change_character_board(board)
    display_grid(grid)


def display_life(life):
    if life == 3:
        with open("Menu/life_3.txt", 'r') as heart:
            line = heart.readline()
            while line != "":
                print(line[:-1])
                line = heart.readline()
    if life == 2:
        with open("Menu/life_2.txt", 'r') as heart:
            line = heart.readline()
            while line != "":
                print(line[:-1])
                line = heart.readline()
    if life == 1:
        with open("Menu/life.txt", 'r') as heart:
            line = heart.readline()
            while line != "":
                print(line[:-1])
                line = heart.readline()


def display_score(score):
    print("==============================")
    print("Score :", score)
    print("==============================")


def display_piece(playable_pieces, piece_choice):
    for i in range(5):
        if i == 4:
            line = modify_functions.change_character_piece(playable_pieces[int(piece_choice)][i])
            line = line[:1] + "■" + line[2:]
        else:
            line = modify_functions.change_character_piece(playable_pieces[int(piece_choice)][i])
        print(line)


def display_pieces_zen_mode(playable_pieces):
    times = int((len(playable_pieces.keys())) // 10)
    for j in range(times):
        for k in range(5):
            for l in range(1, 11):
                line = modify_functions.change_character_piece(playable_pieces[l + (j*10)][k])
                if k == 2:
                    if (l+(10*j)) < 10:
                        print("   ", str(l+(10*j)) + ":", line, end="")
                    else:
                        print("  ", str(l + (10*j)) + ":", line, end="")
                else:
                    print("      ", line, end="")
            print()
        print()
    for q in range(5):
        for l in range(1, (len(playable_pieces.keys()) % 10)+1):
            line = modify_functions.change_character_piece(playable_pieces[l + (times*10)][q])
            if q == 2:
                if (l + (times*10)) < 10:
                    print("   ", str(l + (times*10)) + ":", line, end="")
                else:
                    print("  ", str(l + (times*10)) + ":", line, end="")
            else:
                print("      ", line, end="")
        print()
    print()


def display_pieces_defi_modev3(playable_pieces):
    chosen_piece = game_functions.select_3_random_piece_keys(playable_pieces)
    for k in range(5):
        for j in range(len(chosen_piece)):
            line = modify_functions.change_character_piece(playable_pieces[chosen_piece[j]][k])
            if k == 2:
                if chosen_piece[j] < 10:
                    print("   ", str(chosen_piece[j]) + ":", line, end="")
                else:
                    print("  ", str(chosen_piece[j]) + ":", line, end="")
            else:
                print("      ", line, end="")
        print()
    print()


def display_pieces(game_mode, playable_pieces):
    if game_mode == "Zen":
        display_pieces_zen_mode(playable_pieces)
    else:
        display_pieces_defi_modev3(playable_pieces)


def display_game1(life, score, board, pieces, initial_parameters):
    print("\n" * 20)
    display_life(life)
    print()
    display_score(score)
    print()
    display_grid(modify_functions.change_character_board(board))
    print()
    display_pieces(initial_parameters[1], pieces)
    print()


def display_game2(life, score, board, pieces, piece_choice):
    print("\n" * 20)
    display_life(life)
    print()
    display_score(score)
    print()
    display_grid(modify_functions.change_character_board(board))
    print()
    display_piece(pieces, piece_choice)
    print()
