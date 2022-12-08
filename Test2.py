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


def select_playable_pieces(board):
    matrice_of_pieces = other_functions.transfer_pieces_to_dictionary("common") + other_functions.transfer_pieces_to_dictionary(board)


matrice_of_pieces = select_playable_pieces("common") + select_playable_pieces("circle")
print(matrice_of_pieces)