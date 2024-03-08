class Arbre():
    """
    Une classe pour représenter un arbre avec son label et sa branche mère mb
    """
    
    def __init__(self, label, mb, childs):
        self.label = label
        self.mb = mb
        self.childs = childs

    def __str__(self):
        """
        Allows to read the informations about the question

        Returns
        -------
        str

        """
        return f"Label : {self.label}\Mb : {self.mb}\n"
    
    def get_label(self):
        return self.label

    def get_mb(self):
        return self.mb
    
    def set_label(self, new_label):
        self.label = new_label

    def set_mb(self, new_mb):
        self.mb = new_mb