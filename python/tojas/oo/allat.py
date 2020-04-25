class Allat:
    ehseg = 50
    szomjusag = 50

    def eszik(self):
        self.ehseg -= 1

    def iszik(self):
        self.szomjusag -= 1

    def jatszik(self):
        self.ehseg += 1
        self.szomjusag += 1

allat = Allat()
allat.jatszik()
allat.eszik()
print(allat.ehseg, allat.szomjusag)