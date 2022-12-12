import other_functions
import game_functions
import navigate_functions
import display_functions

#chaine = "Bonjour"
#liste = []
#liste_2 = []
#print(chaine)
#for character in chaine:
#    liste.append(character)
#print(liste)
#print(liste_2)
#for i in range(len(liste)):
#    if liste[i] == "o":
#        liste[i] = 'L'
#print(liste)


#board = "triangle"

#with open("Pieces/common_pieces.txt", "r") as common_pieces:
    #contenu1 = common_pieces.read()
#with open("Pieces/" + board + "_pieces.txt", "r") as special_pieces:
    #contenu2 = special_pieces.read()
#liste_1 = contenu1.split("\n")
#liste_2 = contenu2.split(("\n"))
#common_pieces = tuple(liste_1)
#special_pieces = tuple(liste_2)
#playable_pieces = common_pieces + special_pieces

def RandPiece(transfer_pieces_to_dictionary(choose_board())):       #Là j'ai pris 3 keys aléatoire et il faut maintenant afficher à un endroit les 3 pièces choisi. Incruster dans le prog une fonction display
    import random                                                   #Je sais pas pourquoi mais je peux pas essayer la fonction donc je sais pas si elle marche
    ChosenPiece = []
    for i in range(3):
        ChosenPiece[i] = playable_pieces[random.randint(1, len(playable_pieces.keys()))]
    return ChosenPiece

def Display_ChosenPiece():                                          #La j'affiche les 3 pièces
    print(playable_pieces[ChosenPiece[0]], playable_pieces[ChosenPiece[1]], playable_pieces[ChosenPiece[2]])

def PlacePiece():
    Choix = int(input("Pour choisir la première pièce, tapez 1. Pour choisir la deuxième pièces, tapez 2. Pour choisir la troisième pièce, tapez 3. Pour appeller le service client, tapez 4."))
    L = [][]
    ligne = str(input("Choisissez la ligne : "))
    colonne = str(input("choisissez la colonne : "))
    while (64 < ord(ligne) < 91) and (96 < ord(colonne) < 123):         #Ascii de A à Z et de a à z
        ligne = str(input("Choisissez la ligne : "))
        colonne = str(input("choisissez la colonne : "))
    
    
def validPlacement(liste):
    v = 0
    for i in range():
        for j in range():
            if liste[i][j] > 2:
                v = 1
    if v == 1:
        return False
    else:
        return True
                
            
            



