chaine = "Bonjour"
liste = []
liste_2 = []
print(chaine)
for character in chaine:
    liste.append(character)
print(liste)
print(liste_2)
for i in range(len(liste)):
    if liste[i] == "o":
        liste[i] = 'L'
print(liste)