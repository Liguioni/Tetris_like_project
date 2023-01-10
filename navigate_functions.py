import display_functions
import game_functions


def navigate_welcome():
    choice = ""
    print("\n" * 20)
    display_functions.display_welcome()
    while choice not in ("1", "2"):
        print()
        choice = input(">>")
    if choice == "1":
        game_functions.play()
    elif choice == "2":
        navigate_rules()


def navigate_rules():
    display_functions.display_rules()
    choice = ""
    while choice != "1":
        print("")
        print("Appuyez sur 1 pour retourner à l'accueil.")
        print("")
        choice = input(">>")
    navigate_welcome()
