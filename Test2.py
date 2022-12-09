import other_functions

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


board = "triangle"

with open("Pieces/common_pieces.txt", "r") as common_pieces:
    contenu1 = common_pieces.read()
with open("Pieces/" + board + "_pieces.txt", "r") as special_pieces:
    contenu2 = special_pieces.read()
liste_1 = contenu1.split("\n")
liste_2 = contenu2.split(("\n"))
common_pieces = tuple(liste_1)
special_pieces = tuple(liste_2)
playable_pieces = common_pieces + special_pieces
