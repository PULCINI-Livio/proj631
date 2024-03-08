import csv
import data_test
import math
import structure_donnees as sd

def lecture(csvfile):
    """
    enregistre les données de manière organisé

    Returns
    -------
    list

    """
    data_final = {"liste_attributs":None, "liste_valeur_possible":{}, "donnees":[]}

    #extraction csv dans tableau
    csv_to_list = [] #tableau de tableaux

    with open(csvfile, 'r') as file:
        reader = csv.reader(file)
        csv_to_list.append(next(reader))  # Ajout de l'en-tête de colonne
        for row in reader:
            csv_to_list.append(row)
    
    data_final["liste_attributs"] = csv_to_list[0] #remplissage de la liste d'attributs

    #creation des clés pour les listes de valeurs possibles
    # acces valeur data["liste_valeur_possible"][]

    for att in data_final["liste_attributs"]:
        valeurs_possibles = []
        
        for val in data["liste_attributs"](1,5):

        data["liste_valeur_possible"][att] = valeurs_possibles
    
    #remplissage des valeur des clés
    






lecture("donnees/golf.csv")

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


def E(A:sd.Arbre) -> float:
    """
    summary

    Returns
    -------
    float

    """
    pass


def gain(A:sd.Arbre)-> float:
    """
    summary

    Returns
    -------
    float

    """
    pass