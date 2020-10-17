from allatoooooooook import Allat

class Farm:
    def __init__(self, capacity):
        self.allatok = []
        self.capacity = capacity
    def breed(self):
        if len(self.allatok <= self.capacity):
            allat = Allat()
            self.allatok.append(allat)
    def slaughter(self):
        legkevesbe_ehes_allat = None
        ehseg = self.allatok[0].ehseg
        i = 0
        while i < len(self.allatok):
            if self.allatok[i].ehseg < ehseg:
                legkevesbe_ehes_allat = self.allatok[i]
                ehseg = self.allatok[i].ehseg
            i += 1
        self.allatok.remove(legkevesbe_ehes_allat)
        return legkevesbe_ehes_allat.ehseg

farm = Farm(4)

kutya = Allat()
macska = Allat()
diszno = Allat()

farm.allatok.append(kutya)
farm.allatok.append(macska)
farm.allatok.append(diszno)

print(len(farm.allatok))

diszno.ehseg = 15

print(farm.slaughter())
print(len(farm.allatok))

