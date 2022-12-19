# Tetris_like_project by Berger Luc & Thebault Raphaël
A little school project to create a game that looks like tetris.

Le projet est composé de 8 fichiers  .py
Parmi ces 8, 2 ont servi à tester des programmes, 5 contiennent toutes les fonctions nécessaires au bon fonctionnement du jeu et 
le dernier nommé "Start.py" sert à lancer le jeu (run le programme).
Les 5 fichiers .py contenant les fonctions sont:
        - display_functions.py qui contient toute les fonction servant à afficher
	
        - game_functions.py qui contient les fonctions essentielles servant à jouer:
                      la fonction play qui est le noyau du jeu, elle relie toute les fonctions et permet de les enchainer pour faire fonctionner le jeu.
                      la fonction verify qui vérifie si l'emplacement de la pièce est valide
		      
        - select_functions.py qui contient les fonctions servant a sélectionner le plateau, le mode de jeu, la pièce, et les coordonnés.
	
        - navigate_functions.py qui permet de naviguer entre l'accueuil, les règles et le jeu.
	
        - modify_functions.py qui permet de changer le type de certaines variable pour faciliter leurs utilisations dans d'autres fonctions.

Une fois le programme lancé, l'utilisateur arrive sur le menu qui lui propose deux choix, taper 1 et choisir les paramètres de la partie, ou taper 2 et lire les règles.
Pour partir du fichier règles, il suffit au joueur de taper 1.

Lors du choix des paramètres,  le joueur a d'abord le choix entre 3 plateaux de jeu:
	- Un plateau losange 
	- Un plateau cercle
	- Un plateau triangle
Ensuite, le joueur doit choisir entre 2 modes de jeu:
	- Le mode Zen, le joueur peux placer n'importe quelle pièce de son choix à chaque tour
	- Le mode Défi, le joueur peux placer une parmi 3 pièces choisies aléatoirement.

Suite à cette étape le jeu commence.

	Mode Zen: Toutes les pièces sont affichées à côté d'un numéro. Le joueur tape le numéro de la pièce qu'il veut jouer. 
  Ensuite, il faut choisir l'emplacement de la pièce. Pour cela, seule la pièce choisie est affichée avec un carré blanc. 
  Les coordonnés sont à rentrés sous la forme : Aa. Avec 'A' la ligne et 'a' la colonne.
	Attention: les coordonnés rentrés correspondent à l'emplacement que le carré blanc va remplacer.

	Mode Défi: 3 pièces sont choisies et affichées aléatoirement à côté du numéro qui leur correspondent. Le joueur tape le numéro de la pièce qui l'intéresse. 
  Ensuite, il faut choisir l'emplacement de la pièce. Pour cela, seule la pièce choisie est affichée avec un carré blanc. 
  Les coordonnés sont à rentrés sous la forme : Aa. Avec 'A' la ligne et 'a' la colonne.
  Attention: les coordonnés rentrés correspondent à l'emplacement que le carré blanc va remplacer.

