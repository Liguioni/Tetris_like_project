import other_functions


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
    matrice = other_functions.transform_board_into_matrice(board)
    grid = other_functions.change_character(matrice)
    display_grid(grid)


def display_circle():
    board = "circle"
    matrice = other_functions.transform_board_into_matrice(board)
    grid = other_functions.change_character(matrice)
    display_grid(grid)


def display_triangle():
    board = "triangle"
    matrice = other_functions.transform_board_into_matrice(board)
    grid = other_functions.change_character(matrice)
    display_grid(grid)


def display_3_boards():
    display_diamond()
    print("")
    display_circle()
    print("")
    display_triangle()


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


def display_pieces_Zen_mode(playable_pieces):
    times = (len(playable_pieces.keys()) - (len(playable_pieces.keys()) // 10)) / 10
    for j in range(times):
        for k in range(5):
            if k != 2:
                print("    " + playable_pieces[1 + j * 10][k], end="     ")
            for l in range(2, 11):
                if k == 2:
                    print(l, ":", playable_pieces[l + j*10][k], end=" ")
                else:
                    print(playable_pieces[l + j*10][k], end="     ")
            print()
        print()
    for p in range(len(playable_pieces.keys()) // 10):
        if p != 2:
            print("    " + playable_pieces[1 + times * 10][p], end="     ")
        for l in range(2, 11):
            if p == 2:
                print(l, ":", playable_pieces[l + times*10][p], end=" ")
            else:
                print(playable_pieces[l + times*10][p], end="     ")
        print()
    print()


def display_pieces(game_mode, playable_pieces):
    if game_mode == "Zen":
        display_pieces_Zen_mode(playable_pieces)
    else:
        print("non")