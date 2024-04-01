# PROJ631-Arbres de décision – de Id3 à C4.5

L'objectif de ce projet est de se familiariser avec la notion d'arbre de décision.
J'ai donc créé un programme pour m'aider dans cette tâche

Voir [Sujet Id3.pdf](Sujet Id3.pdf) pour le sujet complet.

Le programme se décompose en plusieurs parties:
    -[fcts_math_et_conversion_donnees.py](Proj/fcts_math_et_conversion_donnees.py) qui contient principalement les fonctions mathématiques trouvées dans l'article de référence \n
    -[Quinlan1986_Article_InductionOfDecisionTrees.pdf](Quinlan1986_Article_InductionOfDecisionTrees.pdf). Donc des fonctions qui vont surtout servir pour d'autres fonctions. \n
    -[structure_donnees.py](Proj/structure_donnees.py) qui contient la classe NoeudDecision ainsi que ses méthodes qui représente l'arbre. \n
    -[tree_build.py](Proj/tree_build.py) qui contient les fonctions de construction de l'arbre, de prédiction, de génération de la matrices ainsi que des fonctions en cours de développement comme celle du post-élagage de l'arbre. \n
    -[zone_test.py](Proj/zone_test.py) permet de générer des arbres avec différentes méthodes d'évaluation, des dictionnaires, des matrices de confusion, etc... \n


Liste des modules/bibliothèques utilisées:
```python
import csv
import math
import copy
```


