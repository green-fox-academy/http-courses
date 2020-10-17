class Allat:
    def __init__(self):
        self.ehseg = 50
        self.szomj = 50
        
    def eszik(self):
        self.ehseg -= 1

    def iszik(self):
        self.szomj -= 1

    def jatszik(self):
        self.szomj += 1
        self.ehseg += 1

oroszlan = Allat()

oroszlan.jatszik()

print(oroszlan.ehseg)
print(oroszlan.szomj)