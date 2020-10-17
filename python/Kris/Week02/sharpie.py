class Sharpie:
    def __init__(self, szin, vastagsag):
        self.szin = szin
        self.vastagsag = vastagsag
        self.tinta_mennyiseg = 100
    def use(self):
        self.tinta_mennyiseg -= 1