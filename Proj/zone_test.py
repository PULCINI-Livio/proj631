from tree_build import *

#Affichage du "codex", un dictionnaire organisé pour construire l'arbre issue des données d'entrainement
codex = lecture("donnees/golf_app.csv")
print("codex")
print(codex)

#Version moins visuelle n'incluant pas les branches "null"
tree_fct_gain = tree_build_fct("donnees/golf_app.csv","gain")
print("Arbre avec la méthode gain:\n")
print(tree_fct_gain)

tree_fct_gr = tree_build_fct("donnees/golf.csv","gain ratio")
print("Arbre avec la méthode gain ratio:\n")
print(tree_fct_gr)

tree_fct_gini = tree_build_fct("donnees/golf_app.csv","gini")
print("Arbre avec la méthode gini:\n")
print(tree_fct_gini)


#Version plus visuelle incluant les branches "null"
tree_visual = tree_build_visual("donnees/golf_app.csv","gain")
print("tree_visual")
print(tree_visual)

#Affichage d'une matrice de confusion avec l'arbre issu des données d'entrainement 
print("matrice de confusion gain")
M_pred_gain = construire_matrice_confusion(tree_fct_gain,"donnees/golf_pred.csv")
print(M_pred_gain)

print("matrice de confusion gain ratio")
M_pred_gr = construire_matrice_confusion(tree_fct_gr,"donnees/golf_pred.csv")
print(M_pred_gr)

print("matrice de confusion gini")
M_pred_gini = construire_matrice_confusion(tree_fct_gini,"donnees/golf_pred.csv")
print(M_pred_gini)

#construction de l'arbre à attributs continue ne fonctionnera pr l'instant que avec la méthode gain ratio (en cours de developpement)
    
        
