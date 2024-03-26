from fcts_math_et_conversion_donnees import *
from structure_donnees import *


def get_best_att(codex:dict):
    """
    Retourne l'attribut ayant le meilleur gain

    Parameters
    ----------
    codex : dict
        le dictionnaire organisé des données

    Returns
    -------
    best : str
        l'attribut au gain le plus élevé

    """
    list_att = codex["liste_attributs"]
    best = list_att[0]
    for att in list_att[1:-1]:
        if (gain(att,codex)) > gain(best,codex):
            best = att
    if best == -1:
        raise ValueError("Pas de meilleur attribut")
    else:
        return best

def partitionner(att:str, val:str, codex:dict):
    """
    Retourne un dictionnaire contenant seulement les données contenant une certaine valeur d'un attribut en paramètre, 
    retire également l'attribut et ses valeurs du dictionnaire

    Parameters
    ----------
    att : str
        l'attribut 
    val : str
        la valeur de l'attribut
    codex : dict
        le dictionnaire contenant les données organisées

    Returns
    -------
    codex : dict
        un nouveau dictionnaire organisé selon un attribut

    """
    #print(codex)
    #print(codex)

    #Traitement clé liste_attribut
    #print(f"codex avant remove {codex}")
    #print(f"tentative remove({att})")
    if att in codex['liste_attributs']:
        codex['liste_attributs'].remove(att)

    #Traitement clé donnees
    i = 0
    donnees = codex['donnees']
    while i < len(donnees):
        if val in donnees[i]:
            donnees[i].remove(val)
            i += 1
        else:
            donnees.remove(donnees[i])

    #Traitement clé all_valeurs_att_restant
    if att in codex['all_valeurs_att_restant']:
        codex['all_valeurs_att_restant'].pop(att)
    
    #Traitement clé liste_valeurs_possibles
    if att in codex['liste_valeurs_possibles']:
        codex['liste_valeurs_possibles'].pop(att)

    #Vérification que les valeurs possibles sont toutes présentes dans les donnees
    for attribut in codex['liste_attributs']:
        for valeur in codex['liste_valeurs_possibles'][attribut]:
            possible = False
            for donnee in donnees:
                if valeur in donnee:
                    possible = True # La valeur existe dans les donnees
            if not possible:
                codex['liste_valeurs_possibles'][attribut].remove(valeur)
    #print(f"codex après partition :{codex}")
    return codex
            

def tree_build_fct(csvfile:str):
    """
    Retourne l'arbre créé à partir des données fournis en paramètre
    N'affiche pas les branches null
    Parameters
    ----------
    csvfile : str
        le nom du fichier contenant les données d'entrainement

    Returns
    -------
    res : Arbre
        l'arbre issu des données d'entrainement

    """
    codex = lecture(csvfile)

    return tree_build_fct_bis(codex)
    


def tree_build_fct_bis(codex:dict):
    """
    Retourne l'arbre créé à partir des données fournis en paramètre
    N'affiche pas les branches null

    Parameters
    ----------
    codex : dict
        le dictionnaire contenant les données organisées

    Returns
    -------
    res : Arbre
        l'arbre issu des données d'entrainement

    """
    
    #Condition d'arret 1: L’ensemble d’exemples associés au noeud courant est vide.
    
    if codex["donnees"] == []:
        return NoeudDecision(resultat="null")

    #Condition d'arret 2: Tous les exemples d’apprentissage associés au noeud courant ont la même valeur de classe,
    #auquel cas une feuille avec cette valeur de classe est retournée.
    if len(list(codex["liste_valeurs_possibles"].values())[-1]) == 1: #On va chercher la ou les valeurs de classe
        return NoeudDecision(resultat = list(codex["liste_valeurs_possibles"].values())[-1][0])
    
    #Condition d'arret 3: Tous les attributs ont été utilisés sur la branche en cours de développement, auquel cas une
    #feuille est retournée avec la classe majoritaire parmi les exemples associés au noeud courant.
    if len(codex["liste_attributs"]) == 1: # il ne reste que la classe
        val1 = list(codex["liste_valeurs_possibles"].values())[-1][0]
        val2 = list(codex["liste_valeurs_possibles"].values())[-1][1]
        liste = codex["donnees"]

        if occurence_val(val1,liste) > occurence_val(val2,liste):
            return NoeudDecision(resultat=val1)
        elif occurence_val(val1,liste) < occurence_val(val2,liste):
            return NoeudDecision(resultat=val2)
        else:
            return NoeudDecision()


    best_att = get_best_att(codex)
    #print(f"best attribut: {best_att}")

    #liste_vals_best_att = codex["all_valeurs_att_restant"][best_att] #version null
    liste_vals_best_att = codex["liste_valeurs_possibles"][best_att]    # version pas de null 
    
    sous_arbre = {}
    for val in liste_vals_best_att:
        codex_copy = copy.deepcopy(codex)
        #print(val)
        sous_arbre[val] = tree_build_fct_bis(partitionner(best_att,val,codex_copy))
        
    return NoeudDecision(attribut=best_att, branches=sous_arbre)
    
def tree_build_visual(csvfile:str):
    """
    Retourne l'arbre créé à partir des données fournis en paramètre
    Affiche les branches null
    Parameters
    ----------
    csvfile : str
        le nom du fichier contenant les données d'entrainement

    Returns
    -------
    res : Arbre
        l'arbre issu des données d'entrainement

    """
    codex = lecture(csvfile)

    return tree_build_visual_bis(codex)
    


def tree_build_visual_bis(codex:dict):
    """
    Retourne l'arbre créé à partir des données fournis en paramètre
    Affiche les branches null

    Parameters
    ----------
    codex : dict
        le dictionnaire contenant les données organisées

    Returns
    -------
    res : Arbre
        l'arbre issu des données d'entrainement

    """
    
    #Condition d'arret 1: L’ensemble d’exemples associés au noeud courant est vide.
    
    if codex["donnees"] == []: 
        return NoeudDecision(resultat="null")

    #Condition d'arret 2: Tous les exemples d’apprentissage associés au noeud courant ont la même valeur de classe,
    #auquel cas une feuille avec cette valeur de classe est retournée.
    if len(list(codex["liste_valeurs_possibles"].values())[-1]) == 1: #On va chercher la ou les valeurs de classe
        return NoeudDecision(resultat = list(codex["liste_valeurs_possibles"].values())[-1][0])
    
    #Condition d'arret 3: Tous les attributs ont été utilisés sur la branche en cours de développement, auquel cas une
    #feuille est retournée avec la classe majoritaire parmi les exemples associés au noeud courant.
    if len(codex["liste_attributs"]) == 1: # il ne reste que la classe
        val1 = list(codex["liste_valeurs_possibles"].values())[-1][0]
        val2 = list(codex["liste_valeurs_possibles"].values())[-1][1]
        liste = codex["donnees"]
        if occurence_val(val1,liste) > occurence_val(val2,liste):
            return NoeudDecision(resultat=val1)
        elif occurence_val(val1,liste) < occurence_val(val2,liste):
            return NoeudDecision(resultat=val2)
        else:
            return NoeudDecision()


    best_att = get_best_att(codex)
    #print(f"best attribut: {best_att}")

    liste_vals_best_att = codex["all_valeurs_att_restant"][best_att] #version null
    #liste_vals_best_att = codex["liste_valeurs_possibles"][best_att]    # version pas de null 
    
    sous_arbre = {}
    for val in liste_vals_best_att:
        codex_copy = copy.deepcopy(codex)
        #print(val)
        sous_arbre[val] = tree_build_visual_bis(partitionner(best_att,val,codex_copy))
        
    return NoeudDecision(attribut=best_att, branches=sous_arbre)

def occurrence_classe_donnees(file:str):
    """
    renvoie le nombre d'occurrence des deux valeurs de classe pour un jeu de données

    Parameters
    ----------
    file : str
        le nom du fichier contenant les données d'entrainement

    Returns
    -------
    res : dict
        un dictionnaire contenant les occurrences
    """
    return lecture(file)["occurrence"]

def occurrence_classe_tree(file:str):
    """
    renvoie le nombre d'occurrence des deux valeurs de classe pour un arbre de décision

    Parameters
    ----------
    file : str
        le nom du fichier contenant les données d'entrainement

    Returns
    -------
    res : dict
        un dictionnaire contenant les occurrences
    """
    tree = tree_build_fct(file)
    #print("tree: ")
    #print(tree)
    valeurs = list(occurrence_classe_donnees(file).keys())
    res = {}
    for val in valeurs:
        res[val] = occurrence_tree_bis(tree,val)
    return res

def occurrence_tree_bis(tree:NoeudDecision,val:str):
    """
    renvoie le nombre d'occurrence d'une valeur de classe pour un arbre de décision

    Parameters
    ----------
    tree : NoeudDecision
        l'arbre à parcourir

    Returns
    -------
    res : int
        l'occurrence de la valeur dans l'arbre
    """
    #print(type(tree))
    #print("LE TREE")
    #print(tree)
    if tree.resultat != None:#si on arrive à une feuille
        if tree.resultat == val:
            return 1
        else:
            return 0
    res = 0
   
    for branche in tree.branches:
        res += occurrence_tree_bis(tree.branches[branche],val)
    
    return res




def prediction(tree:NoeudDecision,exemple:list):
    """
    renvoie le nombre d'occurrence des deux valeurs de classe pour un arbre de décision

    Parameters
    ----------
    tree : NoeudDecision
        l'arbre à parcourir
    donnee : list
        une liste d'un exemple à prédire
    Returns
    -------
    res : any
        la classe issu de la prédiction
    """
    res = "Valeur par défaut"
    if tree.resultat != None: #Si on arrive à une feuille
        return tree.resultat
    for branche in tree.branches:
        if branche in exemple:
            res = prediction(tree.branches[branche],exemple)
    return res


def construire_matrice_confusion(tree:NoeudDecision, train_file:str):
    """
    Renvoie une matrice de confusion à partir de l'arbre et des donnees d'entrainement

    Parameters
    ----------
    tree : NoeudDecision
        l'arbre à parcourir
    train_file : str
        le nom du fichier contenant les données d'entrainement

    Returns
    -------
    res : int
        l'occurrence de la valeur dans l'arbre
    """
    matrice_confusion = {}
    classes = set()  # Ensemble des classes possibles
    codex = lecture(train_file)
    
    # Récupérer les classes possibles à partir des données d'entraînement
    for exemple in codex["donnees"]:
        classes.add(exemple[-1])  # La classe est la dernière valeur de chaque exemple
    
    # Initialiser la matrice de confusion avec des comptes à zéro
    for classe_reelle in classes:
        matrice_confusion[classe_reelle] = {}
        for classe_predite in classes:
            matrice_confusion[classe_reelle][classe_predite] = 0
    
    # Effectuer les prédictions pour chaque exemple dans les données d'entraînement
    
    for exemple in codex["donnees"]:
        classe_reelle = exemple[-1]  # La vérité de terrain est la dernière valeur
        classe_predite = prediction(tree, exemple)  # Faire une prédiction avec l'arbre
        #print(exemple)
        #print(classe_predite)
        
        
        matrice_confusion[classe_reelle][classe_predite] += 1  # Mettre à jour la matrice de confusion
    
    return matrice_confusion

#-------------------------------#
#-------------TEST--------------#
#-------------------------------#

#print(occurrence_classe_donnees("donnees/golf.csv"))
#print("pour l'arbre")
#print(occurrence_classe_tree("donnees/golf.csv"))
#print("pour les donnees")
#print(occurrence_classe_donnees("donnees/golf.csv"))

#test=["rain","mild","high","false","yes"]
#print(prediction(tree,test))

#print(list(codex["liste_valeurs_possibles"].values())[-1][0])
#donnees = [['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Normal', 'Oui']]
#print(occurence_val('Chaud',donnees))
#codex = {'liste_attributs': ['Temperature', 'Humidite', 'Jouer au tennis'], 'liste_valeurs_possibles': {'Jouer au tennis': ['Non', 'Oui']}, 'donnees': [['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Normal', 'Oui']]}
#print(list(codex["liste_valeurs_possibles"].values())[-1])
#print(get_best_att(lecture("donnees/golf.csv")))
#print(partitionner("humidity",'high',lecture("donnees/golf.csv")))

#Version moins visuelle n'incluant pas les branches "null"
tree_fct = tree_build_fct("donnees/golf.csv")
print("tree_fct")
print(tree_fct)