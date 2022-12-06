import display_functions
import game_functions


def navigate_welcome():
    choice = 0
    display_functions.display_welcome()
    while choice == 0:
        choice = int(input(">>"))
        if choice != 1:
            if choice != 2:
                choice = 0
    if choice == 1:
        game_functions.play()
    elif choice == 2:
        navigate_rules()


def navigate_rules():
    display_functions.display_rules()
    choice = 0
    while choice != 1:
        print("")
        print("Appuyez sur 1 pour retourner à l'accueil.")
        print("Appuyez sur 2 pour accéder au paramètres.")
        print("")
        choice = int(input(">>"))
    navigate_welcome()