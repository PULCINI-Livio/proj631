# PROJ631-Arbres de décision – de Id3 à C4.5

## INTRO
L'objectif de ce projet est de se familiariser avec la notion d'arbre de décision.
J'ai donc créé un programme pour m'aider dans cette tâche

Voir [Sujet_Id3.pdf](Sujet_Id3.pdf) pour le sujet complet.

## ASPECT TECHNIQUE
Le programme se décompose en plusieurs parties:   
    - [fcts_math_et_conversion_donnees.py](Proj/fcts_math_et_conversion_donnees.py) qui contient principalement les fonctions mathématiques trouvées dans l'article de référence [Quinlan1986_Article_InductionOfDecisionTrees.pdf](Quinlan1986_Article_InductionOfDecisionTrees.pdf). Donc des fonctions qui vont surtout servir pour d'autres fonctions.   
    - [structure_donnees.py](Proj/structure_donnees.py) qui contient la classe NoeudDecision ainsi que ses méthodes qui représente l'arbre.   
    - [tree_build.py](Proj/tree_build.py) qui contient les fonctions de construction de l'arbre, de prédiction, de génération de la matrices ainsi que des fonctions en cours de développement comme celle du post-élagage de l'arbre. La plupart de ces fonctions sont récursives.  
    - [zone_test.py](Proj/zone_test.py) permet de générer des arbres avec différentes méthodes d'évaluation, des dictionnaires, des matrices de confusion, etc...      
    - [donnees](donnees) qui contient les données utilisées pour construire les premiers arbres et qui sont au format .csv.
Liste des modules/bibliothèques utilisées:
```python
import csv
import math
import copy
```

## INSTALLATION
Je le précise au cas où, vous devez avoir Python installé sur votre machine pour faire fonctionner ce programme.  

En respectant la structure des dossiers, télécharger le contenu de [Proj](Proj) pour avoir les fonctions et de [donnees](donnees) pour connaitre la forme des données d'entrainement.  


## MODE D'EMPLOI
Vous n'avez besoin que de manipuler le fichier [zone_test.py](Proj/zone_test.py) en "commentant"/"décommentant" les lignes qui vous intéresse. En lisant la documentation de la fonction ```tree_build_fct()```, vous verrez que le deuxième paramètre défini la méthode d'évaluation/choix des attributs: ```"gain"```,```"gain ratio"``` ou ```"gini"```.    

La matrice de confusion permet de voir le nombre de fois où les prédictions correspondent ou non. Cela a peut d'intérêts quoi on utilise la fonction ```construire_matrice_confusion()``` sur les mêmes données que lors de la création de l'arbre. Vous pouvez par exemple utiliser ```tree_build_fct()``` sur le fichier [golf_app.csv](donnees/golf_app.csv) et ```construire_matrice_confusion()``` sur le fichier [golf_pred.csv](donnees/golf_pred.csv) pour voir l'efficacité de votre arbre. 

Attention à la forme de vos données d'entrainement; le programme ne prend pas encore en compte les données à valeur manquantes, et pas les valeurs continues de manière optimisée (mais vous pouvez toujours essayer cette dernière pour visualiser votre arbre).  

L'affichage des résultats se fait dans le terminal/console de l'application (une version plus visuelle est en cours de développement).  
Vous pouvez donc créer votre propre arbre avec vos propres données d'entrainement.


## CONCLUSION
Ce projet m'a demandé une importante quantité de travail mais il m'a permis d'approfondir le sujet des algorithmes de prédiction et de m'aiguiller un peu plus pour mes futures perspectives sur mon projet professionnel. J'ai pu mettre en pratique des notions apprises récemment ce qui présente un bénéfice certain.

