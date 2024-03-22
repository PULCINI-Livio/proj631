import csv
import math
import copy
def lecture(csvfile:str) -> dict:
    """
    enregistre les données de manière organisé sous forme de dictionnaire

    Parameters
    ----------
    csvfile : un fichier csv avec un header

    Returns
    -------
    dictionnaire de la forme: {"liste_attributs":None, "liste_valeurs_possibles":{}, "donnees":[]}

    """
    codex = {"liste_attributs":None, "liste_valeurs_possibles":{}, "donnees":[], "all_valeurs_att_restant":{}}

    #extraction csv dans tableau
    csv_to_list = [] #tableau de tableaux

    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        csv_to_list.append(next(reader))  # Ajout de l'en-tête de colonne
        for row in reader:
            csv_to_list.append(row)
    
    codex["liste_attributs"] = csv_to_list[0] #remplissage de la liste d'attributs avec l'en-tête de colonne

    #creation des clés pour les listes de valeurs possibles
    # acces valeur data["liste_valeurs_possibles"][]

    csv_to_list_sans_header = csv_to_list[1:] 
    
    if csv_to_list_sans_header != []:
        for i in range(len(csv_to_list_sans_header[0])): # Boucle pour chaque attribut
            valeurs_possibles = []
            # Remplissage des valeurs possible pour le i-eme attribut
            for ensemble in csv_to_list_sans_header: 
                valeurs_possibles.append(ensemble[i])

            # Retirer les doublons
            # Créer un dictionnaire avec les éléments de la liste comme clés et None comme valeurs
            dict_sans_doublons = dict.fromkeys(valeurs_possibles)  
            # Récupérer les clés du dictionnaire sous forme de liste
            liste_sans_doublons = list(dict_sans_doublons.keys())

            # Remplissage du dictionnaire résultat
            att = codex["liste_attributs"][i]
            codex["liste_valeurs_possibles"][att] = liste_sans_doublons
            codex["donnees"] = csv_to_list_sans_header
    codex["all_valeurs_att_restant"] = copy.deepcopy(codex["liste_valeurs_possibles"])
    
    return codex

#print(lecture("donnees/golf.csv"))

def I(p:int, n:int) -> float:
    """
    summary

    Returns
    -------
    float

    """
    if n==0 or p==0:
        return 0
    else:
        return -(p/(p+n))*(math.log2((p/(p+n))))-(n/(n+p))*(math.log2((n/(n+p))))


def pi_ni(i:int, att:str, codex:dict) -> tuple:
    """
    Retourne p (i.e n) le nombre de fois qu'apparait la première (i.e seconde) valeur de l'attribut cible 
    et la i-eme valeur de att dans le codex
    
    Parameters
    ----------
    i : int
        l'index de la valeur de l'attribut dans le codex
    att : str
        l'attribut choisi
    codex : dict
        le dictionnaire organisé des données

    Returns
    -------
    tuple

    """
    p = 0
    n = 0
    valeur_att = codex["liste_valeurs_possibles"][att][i] # Ex: 'sunny' pour i=1 
    target = list(codex["liste_valeurs_possibles"].keys())[-1] # Ex: 'play'
    target_values = codex["liste_valeurs_possibles"][target] # Ex: ['no','yes']

    for donnee in codex["donnees"]: # donnee est un tableau de type ['sunny', 'hot', 'high', 'false', 'no']
        if valeur_att in donnee:
            if target_values[0] in donnee:
                p+=1
            else:
                n+=1
    return (p,n)

#print(pi_ni(2,'outlook',lecture("donnees/golf.csv")))

def p_n(target_att:str, codex:dict) -> tuple:
    """
    Retourne p (i.e n) le nombre de fois qu'apparait la première (i.e seconde) valeur
    de l'attribut cible dans le codex
    
    Parameters
    ----------
    att : str
        l'attribut choisi
    codex : dict
        le dictionnaire organisé des données

    Returns
    -------
    tuple

    """
    p = 0
    n = 0
    target_values = codex["liste_valeurs_possibles"][target_att] # Ex: ['no','yes']
    
    for donnee in codex["donnees"]: # donnee est un tableau de type ['sunny', 'hot', 'high', 'false', 'no']
        if target_values[0] in donnee:
            p+=1
        else:
            n+=1
    return (p,n)



def E(A:str, codex:dict) -> float:
    """
    Calcul une moyenne pondérée

    Parameters
    ----------
    A : str
        un attribut
    codex : dict
        le dictionnaire organisé des données
        
    Returns
    -------
    float

    """
    res = 0
    tuple_p_n = p_n(A,codex)
    for i in range(len(codex["liste_valeurs_possibles"][A])):
        tuple_pi_ni = pi_ni(i,A,codex)
        res += ((tuple_pi_ni[0]+tuple_pi_ni[1])/(tuple_p_n[0]+tuple_p_n[1]))*I(tuple_pi_ni[0],tuple_pi_ni[1])
    return res

#print(E("outlook",lecture("donnees/golf.csv")))



def gain(A:str, codex:dict) -> float:
    """
    Calcul le gain d'un attribut

    Parameters
    ----------
    A : str
        un attribut
    codex : dict
        le dictionnaire organisé des données

    Returns
    -------
    float

    """
    tuple_p_n = p_n(A,codex)
    res = I(tuple_p_n[0],tuple_p_n[1])-E(A,codex)
    return round(res,3)

#print(gain("outlook",lecture("donnees/golf.csv")))
#print(lecture("donnees/golf_copy.csv"))
#print(len(lecture("donnees/golf_copy.csv")["liste_attributs"]))


