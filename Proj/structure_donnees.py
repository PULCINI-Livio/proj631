

class Arbre():
    """
    Une classe pour représenter un arbre avec son label, 
    sa branche mère mb,
    la liste de ses noeuds enfants
    et la liste de ses branches qui le lient à ses enfants
    """
    
    def __init__(self, label, mb, childs, branchs):
        self.label = label
        self.mb = mb
        self.childs = childs
        self.branchs = branchs

    def __str__(self):
        """
        affichage des attributs du noeud

        Returns
        -------
        str

        """
        return f"Label : {self.label}\nMb : {self.mb}\nChilds : {self.childs}\nBranchs : {self.branchs}\n"
    
    # Getters and Setters
    def get_label(self):
        return self.label

    def get_mb(self):
        return self.mb
    
    def get_childs(self):
        return self.childs
    
    def get_branchs(self):
        return self.branchs
    
    def set_label(self, new_label):
        self.label = new_label

    def set_mb(self, new_mb):
        self.mb = new_mb

    def set_childs(self, new_childs):
        self.childs = new_childs

    def set_branchs(self, new_branchs):
        self.branchs = new_branchs
        
        
    def add_child(self, new_child):
        self.childs.append(new_child)

    def add_branch(self, new_branch):
        self.branchs.append(new_branch)
    