

class NoeudDecision:
    def __init__(self, attribut:str=None, valeur=None, branches=None, resultat=None):
        """

        Parameters
        ----------
        attribut : str
            Attribut sur lequel se fait la division
        valeur : 
            Valeur de l'attribut pour cette division
        branches : dict
            Sous-arbres pour chaque valeur de l'attribut
        resultat  
            Résultat (étiquette de classe) pour ce nœud s'il est une feuille

        """
        
        self.attribut = attribut  # Attribut sur lequel se fait la division
        self.valeur = valeur  # Valeur de l'attribut pour cette division
        self.branches = branches if branches is not None else {}  # Sous-arbres pour chaque valeur de l'attribut
        self.resultat = resultat  # Résultat (étiquette de classe) pour ce noeud s'il est une feuille

    def __str__(self, niveau=0):
        # Construire la chaîne de caractères pour ce nœud
        representation = "  " * niveau
        #if self.attribut is not None:
        representation += f"Attribut: {self.attribut}, "
        
        representation += f"Résultat: {self.resultat}\n"

        # Parcourir récursivement les branches et leurs enfants
        for valeur, enfant in self.branches.items():
            representation += "  " * (niveau + 1) + f"Valeur: {valeur}\n"
            representation += enfant.__str__(niveau + 2)  # Appel récursif pour l'enfant

        return representation
    
 
    
    