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

Test
teste

