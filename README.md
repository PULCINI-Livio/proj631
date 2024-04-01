# PROJ631-Arbres de décision – de Id3 à C4.5

## INTRO
L'objectif de ce projet est de se familiariser avec la notion d'arbre de décision.
J'ai donc créé un programme pour m'aider dans cette tâche

Voir [Sujet_Id3.pdf](Sujet_Id3.pdf) pour le sujet complet.

Le programme se décompose en plusieurs parties:   
    - [fcts_math_et_conversion_donnees.py](Proj/fcts_math_et_conversion_donnees.py) qui contient principalement les fonctions mathématiques trouvées dans l'article de référence.   
    - [Quinlan1986_Article_InductionOfDecisionTrees.pdf](Quinlan1986_Article_InductionOfDecisionTrees.pdf). Donc des fonctions qui vont surtout servir pour d'autres fonctions.   
    - [structure_donnees.py](Proj/structure_donnees.py) qui contient la classe NoeudDecision ainsi que ses méthodes qui représente l'arbre.   
    - [tree_build.py](Proj/tree_build.py) qui contient les fonctions de construction de l'arbre, de prédiction, de génération de la matrices ainsi que des fonctions en cours de développement comme celle du post-élagage de l'arbre.   
    - [zone_test.py](Proj/zone_test.py) permet de générer des arbres avec différentes méthodes d'évaluation, des dictionnaires, des matrices de confusion, etc...   

Liste des modules/bibliothèques utilisées:
```python
import csv
import math
import copy
```

## INSTALLATION

En respectant la structure des dossiers, télécharger le contenu de [Proj](Proj) pour avoir les fonctions et de [donnees](donnees) pour connaitre la forme des données d'entrainement.  
Vous n'avez besoin que de manipuler le fichier [zone_test.py](Proj/zone_test.py) en "commentant"/"décommentant" les lignes qui vous intéresse. En lisant la documentation de la fonction ```tree_build_fct()```




