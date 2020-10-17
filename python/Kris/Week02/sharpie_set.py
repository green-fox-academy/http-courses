class SharpieSet:
    def __init__(self):
        self.sharpies = []
    def add(self, sharpie):
        self.sharpies.append(sharpie)
    def count_usable(self):
        hasznalhatok = []
        for sharpie in self.sharpies:
            if sharpie.tinta_mennyiseg > 0:
                hasznalhatok.append(sharpie.szin)
        return hasznalhatok
    def remove_trash(self):
        i = 0
        while i < len(self.sharpies):
            if self.sharpies[i].tinta_mennyiseg <= 0:
                self.sharpies.remove(self.sharpies[i])
                continue
            i += 1
        # vagy a tomb egy copyján végigmenni, de az eredetiből törölni
        # for sharpie in self.sharpies[:]:
        #     if sharpie.tinta_mennyiseg <= 0:
        #         self.sharpies.remove(sharpie)
    def printList(self):
        sharpiek = []
        for sharpie in self.sharpies:
            sharpiek.append({sharpie.szin: sharpie.tinta_mennyiseg})
        print(sharpiek)

