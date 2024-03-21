from fcts_math_et_conversion_donnees import *
from structure_donnees import *
import pandas as pd


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

def partitionner(att:str, val:str, codex_old:dict):
    """
    Retourne un dictionnaire contenant seulement les données contenant une certaine val d'un attribut en paramètre, 
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
    #IMPORTANT faire une copie du dictionnaire
    codex = codex_old.copy()

    #Traitement clé liste_attribut
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

    #Traitement clé liste_valeurs_possibles
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
            
    return codex
            


def tree_build(csvfile:str):
    """
    Retourne l'arbre créé à partir des données fournis en paramètre

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

    tree_build_bis(codex)
    


def tree_build_bis(codex:dict):
    """
    Retourne l'arbre créé à partir des données fournis en paramètre

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
        pass

    #Condition d'arret 2: Tous les exemples d’apprentissage associés au noeud courant ont la même valeur de classe,
    #auquel cas une feuille avec cette valeur de classe est retournée.
    if len(codex["liste_valeurs_possibles"].popitem()[1]) == 1: #On va chercher la ou les valeurs de classe
        pass
    
    #Condition d'arret 3: Tous les attributs ont été utilisés sur la branche en cours de développement, auquel cas une
    #feuille est retournée avec la classe majoritaire parmi les exemples associés au noeud courant.
    if codex["liste_attributs"] == 1:
        pass

    best_att = get_best_att(codex)
    abr = Arbre(best_att,None,None,[codex["liste_valeurs_possibles"][best_att]])
    partitionner()
        

#print(lecture("donnees/golf_copy.csv"))




#-------------------------------#
#-------------TEST--------------#
#-------------------------------#
