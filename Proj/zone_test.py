from tree_build import *

#Affichage du "codex", un dictionnaire organisé pour construire l'arbre issue des données d'entrainement
codex = lecture("donnees/golf_app.csv")
print("codex")

#Version moins visuelle n'incluant pas les branches "null"
tree_fct = tree_build_fct("donnees/golf.csv")
print("tree_fct")
print(tree_fct)

#Version plus visuelle incluant les branches "null"
tree_visual = tree_build_visual("donnees/golf.csv")
print("tree_visual")
print(tree_visual)

#Affichage d'une matrice de confusion avec l'arbre issu des données d'entrainement 
print("matrice de confusion")
M_pred = construire_matrice_confusion(tree_fct,"donnees/golf.csv")
print(M_pred)

