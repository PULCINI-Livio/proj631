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
    print(codex)
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
            

def occurence_val(val,l:list):
    """
    Retourne le nombre de liste dans une liste de liste qui contiennent la valeur

    Parameters
    ----------
    val : Any
        la valeur dont on veut connaitre l'occurence
    l : list
        la liste de liste à parcourir
    Returns
    -------
    res : int
        l'occurence de val dans les listes

    """
    res = 0
    # On parcours les sous-listes

    for sl in l: 
        if val in sl:
            res += 1
    return res





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

    return tree_build_bis(codex)
    


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
        print(1111111111)
        return NoeudDecision(resultat="null")

    #Condition d'arret 2: Tous les exemples d’apprentissage associés au noeud courant ont la même valeur de classe,
    #auquel cas une feuille avec cette valeur de classe est retournée.
    if len(list(codex["liste_valeurs_possibles"].values())[-1]) == 1: #On va chercher la ou les valeurs de classe
        return NoeudDecision(resultat = list(codex["liste_valeurs_possibles"].values())[-1][0])
    
    #Condition d'arret 3: Tous les attributs ont été utilisés sur la branche en cours de développement, auquel cas une
    #feuille est retournée avec la classe majoritaire parmi les exemples associés au noeud courant.
    if len(codex["liste_attributs"]) == 1:
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
    print("best attribut :" + best_att)
    liste_vals_best_att = codex["all_valeurs_att_restant"][best_att]
    
    sous_arbre = {}
    for val in liste_vals_best_att:
        codex_copy = copy.deepcopy(codex)
        print(val)
        sous_arbre[val] = tree_build_bis(partitionner(best_att,val,codex_copy))
        
    return NoeudDecision(attribut=best_att, branches=sous_arbre)
    


#codex = lecture("donnees/golf_copy.csv")
#print(list(codex["liste_valeurs_possibles"].values())[-1][0])



#-------------------------------#
#-------------TEST--------------#
#-------------------------------#
#donnees = [['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Normal', 'Oui']]
#print(occurence_val('Chaud',donnees))
#codex = {'liste_attributs': ['Temperature', 'Humidite', 'Jouer au tennis'], 'liste_valeurs_possibles': {'Jouer au tennis': ['Non', 'Oui']}, 'donnees': [['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Haute', 'Non'], ['Chaud', 'Normal', 'Oui']]}
#print(list(codex["liste_valeurs_possibles"].values())[-1])

print(tree_build("donnees/golf.csv"))

#print(get_best_att(lecture("donnees/golf.csv")))
#print(partitionner("humidity",'high',lecture("donnees/golf.csv")))