class Pokemon:
    def __init__(self,  nev, tipus, ellenfel):
        self.nev = nev
        self.tipus = tipus
        self.ellenfel = ellenfel

    def hatasos_ellene(self, masik):
        return self.ellenfel == masik.tipus
